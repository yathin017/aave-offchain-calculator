import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from dotenv import load_dotenv
from decimal import Decimal, getcontext
from abi import *
from calc import *

class DataProvider:
    def __init__(self, user_address):
        load_dotenv()

        web3_url = os.getenv('WEB3_PROVIDER')
        self.web3 = Web3(Web3.HTTPProvider(web3_url))

        self.initialize_addresses()
        self.initialize_contracts()
        self.get_reserve_data(self.token_address)
        self.get_slopes_data()
        self.cumulate_user_balance_data(user_address)
        self.current_timestamp = self.web3.eth.get_block('latest').timestamp

    def get_contract(self, contract_address, contract_abi):
        return self.web3.eth.contract(address=contract_address, abi=contract_abi)

    def get_function_value(self, contract, contract_function, *args):
        fn = getattr(contract.functions, contract_function)(*args)
        value = fn.call()
        return value

    def initialize_addresses(self):
        self.lending_pool_addresses_provider_address = os.getenv('LENDING_POOL_ADDRESSES_PROVIDER_ADDRESS')
        self.lending_pool_core_address = os.getenv('LENDING_POOL_CORE_ADDRESS')
        self.lending_pool_address = os.getenv('LENDING_POOL_ADDRESS')
        self.token_address = os.getenv('TOKEN_ADDRESS') # USDC

    def initialize_contracts(self):
        # lending pool addresses provider contract
        self.lending_pool_addresses_provider_contract = self.get_contract(self.lending_pool_addresses_provider_address, lending_pool_addresses_provider_abi)
        # lending pool core contract
        self.lending_pool_core_contract = self.get_contract(self.lending_pool_core_address, lending_pool_core_abi)
        # lending pool contract
        self.lending_pool_contract = self.get_contract(self.lending_pool_address, lending_pool_abi)
        # interest rate strategy contract
        interest_rate_strategy_address = self.get_function_value(self.lending_pool_core_contract, 'getReserveInterestRateStrategyAddress', self.token_address)
        self.interest_rate_strategy_contract = self.get_contract(interest_rate_strategy_address, interest_rate_strategy_abi)
        # aToken contract
        a_token_address = self.get_function_value(self.lending_pool_core_contract, 'getReserveATokenAddress', self.token_address)
        self.a_token_contract = self.get_contract(a_token_address, a_token_abi)

    def get_reserve_data(self, token_address):
        self.reserve_data = self.get_function_value(self.lending_pool_contract, 'getReserveData', token_address)
        print(self.reserve_data)

        self.total_liquidity = self.reserve_data[0]
        self.available_liquidity = self.reserve_data[1]
        self.total_borrows_stable = self.reserve_data[2]
        self.total_borrows_variable =self.reserve_data[3]
        self.liquidity_rate = self.reserve_data[4]
        self.variable_borrow_rate = self.reserve_data[5]
        self.stable_borrow_rate = self.reserve_data[6]
        self.average_stable_borrow_rate = self.reserve_data[7]
        self.utilization_rate = self.reserve_data[8]
        self.liquidity_index = self.reserve_data[9]
        self.variable_borrow_index = self.reserve_data[10]
        self.last_updated_timestamp = self.reserve_data[12]

    def get_slopes_data(self):
        self.base_variable_borrow_rate = self.get_function_value(self.interest_rate_strategy_contract, 'getBaseVariableBorrowRate')
        self.stable_rate_slope_1 = self.get_function_value(self.interest_rate_strategy_contract, 'getStableRateSlope1')
        self.stable_rate_slope_2 = self.get_function_value(self.interest_rate_strategy_contract, 'getStableRateSlope2')
        self.variable_rate_slope_1 = self.get_function_value(self.interest_rate_strategy_contract, 'getVariableRateSlope1')
        self.variable_rate_slope_2 = self.get_function_value(self.interest_rate_strategy_contract, 'getVariableRateSlope2')

    def cumulate_user_balance_data(self, user_address):
        self.previous_principal_balance = self.get_function_value(self.a_token_contract, 'principalBalanceOf', user_address)
        self.a_tokens = self.previous_principal_balance
        print("Initial atokens: ", self.a_tokens)


class InterestRateCalculator(DataProvider):
    SECONDS_PER_YEAR = 365 * 24 * 60 * 60
    OPTIMAL_UTILIZATION_RATE = Decimal('0.45') * Decimal('1e27')
    EXCESS_UTILIZATION_RATE = Decimal('1e27') - OPTIMAL_UTILIZATION_RATE
    getcontext().prec = 30

    def __init__(self, user_address):
        super().__init__(user_address)

    def calculate_linear_interest(self, liquidity_rate, last_updated_timestamp, current_timestamp):
        time_difference = current_timestamp - last_updated_timestamp
        time_delta = rayDiv(wadToRay(time_difference), wadToRay(self.SECONDS_PER_YEAR))
        return rayMul(liquidity_rate, time_delta) + ray()

    def calculate_compounded_interest(self, variable_borrow_rate, last_updated_timestamp, current_timestamp):
        time_difference = current_timestamp - last_updated_timestamp
        rate_per_second = variable_borrow_rate / Decimal(self.SECONDS_PER_YEAR)
        return rayPow(rate_per_second + ray(), time_difference)

    def calculate_cumulative_indexes(self):
        # Linear Interest - Liquidity index
        cumulated_liquidity_interest = self.calculate_linear_interest(self.liquidity_rate, self.last_updated_timestamp, self.current_timestamp)
        new_liquidity_index = rayMul(cumulated_liquidity_interest, self.liquidity_index)
        print("Liquidity Index: ", new_liquidity_index)
        self.liquidity_index = new_liquidity_index

        # Compound Interest - Variable borrow index
        cumulated_variable_borrow_interest = self.calculate_compounded_interest(self.variable_borrow_rate, self.last_updated_timestamp, self.current_timestamp)
        new_variable_borrow_index = rayMul(cumulated_variable_borrow_interest, self.variable_borrow_index)
        print("Variable Borrow Index: ", new_variable_borrow_index)
        self.variable_borrow_index = new_variable_borrow_index

    def get_total_borrows(self):
        return self.total_borrows_stable + self.total_borrows_variable

    def calculate_utilization_rate(self, total_borrows, available_liquidity):
        if total_borrows == 0 and available_liquidity == 0:
            return Decimal(0)
        else:
            return rayDiv(total_borrows, (available_liquidity + total_borrows))

    def calculate_interest_rates(self, amount_deposited, amount_redeemed):
        # Available liquidity
        new_available_liquidity = self.available_liquidity + amount_deposited - amount_redeemed
        print("Available Liquidity: ", new_available_liquidity)
        self.available_liquidity = new_available_liquidity

        # Utilization rate
        new_utilization_rate = self.calculate_utilization_rate(self.get_total_borrows(), self.available_liquidity)
        print("Utilization Rate: ", new_utilization_rate)
        self.utilization_rate = new_utilization_rate
        
        if self.utilization_rate > self.OPTIMAL_UTILIZATION_RATE:
            excess_utilization_rate_ratio = rayDiv((self.utilization_rate - self.OPTIMAL_UTILIZATION_RATE), self.EXCESS_UTILIZATION_RATE)

            # Stable borrow rate
            new_stable_borrow_rate = self.stable_borrow_rate + self.stable_rate_slope_1 + rayMul(self.stable_rate_slope_2, excess_utilization_rate_ratio)
            print("Stable Borrow Rate: ", new_stable_borrow_rate)
            self.stable_borrow_rate = new_stable_borrow_rate

            # Variable borrow rate
            new_variable_borrow_rate = self.base_variable_borrow_rate + variable_rate_slope_1 + rayMul(self.variable_rate_slope_2, excess_utilization_rate_ratio)
            print("Variable Borrow Rate: ", new_variable_borrow_rate)
            self.variable_borrow_rate = new_variable_borrow_rate

        else:
            # Stable borrow rate
            new_stable_borrow_rate = self.stable_borrow_rate + rayMul(self.stable_rate_slope_1, rayDiv(self.utilization_rate, self.OPTIMAL_UTILIZATION_RATE))
            print("Stable Borrow Rate: ", new_stable_borrow_rate)
            self.stable_borrow_rate = new_stable_borrow_rate

            # Variable borrow rate
            new_variable_borrow_rate = self.base_variable_borrow_rate + rayMul(rayDiv(self.utilization_rate, self.OPTIMAL_UTILIZATION_RATE), self.variable_rate_slope_1)
            print("Variable Borrow Rate: ", new_variable_borrow_rate)
            self.variable_borrow_rate = new_variable_borrow_rate

        # Liquidity rate
        if self.get_total_borrows() == 0:
            return 0
        weighted_stable_rate = rayMul(wadToRay(self.total_borrows_stable), self.average_stable_borrow_rate)
        weighted_variable_rate = rayMul(wadToRay(self.total_borrows_variable), self.variable_borrow_rate)
        overall_borrow_rate = rayDiv(weighted_stable_rate + weighted_variable_rate, wadToRay(self.get_total_borrows()))
        new_liquidity_rate = rayMul(overall_borrow_rate, self.utilization_rate)
        print("Liquidity Rate: ", new_liquidity_rate)
        self.liquidity_rate = new_liquidity_rate
        self.current_timestamp = self.current_timestamp

    def normalized_income(self, liquidity_rate, last_updated_timestamp, current_timestamp, liquidity_index):
        cumulated = rayMul(self.calculate_linear_interest(liquidity_rate, last_updated_timestamp, current_timestamp), liquidity_index)
        return cumulated

    def calculate_cumulated_balance(self, user_address, user_balance):
        return rayToWad(rayDiv(rayMul(wadToRay(user_balance), normalized_income(self.liquidity_rate, self.last_updated_timestamp, self.current_timestamp, self.liquidity_index)), self.user_index))

    def get_current_principal_balance(self, user_address):
        if(self.previous_principal_balance==0):
            return 0
        return self.calculate_cumulated_balance(user_address, self.previous_principal_balance)

    def cumulate_balance(self, user_address, amount):
        balance_increase = self.get_current_principal_balance(user_address) - self.previous_principal_balance
        new_principal_balance = self.previous_principal_balance + balance_increase
        # Mint tokens
        new_a_tokens = self.a_tokens + balance_increase
        self.a_tokens = new_a_tokens
        user_index = self.normalized_income(self.liquidity_rate, self.last_updated_timestamp, self.current_timestamp, self.liquidity_index)
        print("User Index: ", user_index)
        return (self.previous_principal_balance, new_principal_balance, balance_increase, user_index)

    def deposit(self, user_address, amount):
        print("=====DEPOSIT=====")
        self.calculate_cumulative_indexes()
        self.calculate_interest_rates(amount, 0)
        self.cumulate_balance(user_address, amount)
        new_a_tokens = self.a_tokens + amount
        print("aUSDC after deposit: ", new_a_tokens)
        self.a_tokens = new_a_tokens

    def redeem(self, user_address, amount):
        print("=====REDEEM=====")
        if(amount > self.a_tokens):
            return "No sufficient funds"
        self.cumulate_balance(user_address, amount)
        new_a_tokens = self.a_tokens - amount
        print("aUSDC after redeem: ", new_a_tokens)
        self.a_tokens = new_a_tokens
        self.calculate_cumulative_indexes()
        self.calculate_interest_rates(0, amount)

def main():
    user_address = '0xE6707721ad79f4519f80D95ef4D961b60893CD76'
    calculator = InterestRateCalculator(user_address)

    # Deposit
    amount_deposited = 10000
    calculator.deposit(user_address, amount_deposited)

    # Redeem
    amount_redeemed = 5000
    calculator.redeem(user_address, amount_redeemed)

if __name__ == '__main__':
    main()