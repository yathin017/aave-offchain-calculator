lending_pool_abi = [
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_borrowRateMode",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_borrowRate",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_originationFee",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_borrowBalanceIncrease",
        "type": "uint256"
      },
      {
        "indexed": True,
        "internalType": "uint16",
        "name": "_referral",
        "type": "uint16"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "Borrow",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      },
      {
        "indexed": True,
        "internalType": "uint16",
        "name": "_referral",
        "type": "uint16"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "Deposit",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_target",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_totalFee",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_protocolFee",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "FlashLoan",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_collateral",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_purchaseAmount",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_liquidatedCollateralAmount",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_accruedBorrowInterest",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "address",
        "name": "_liquidator",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "bool",
        "name": "_receiveAToken",
        "type": "bool"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "LiquidationCall",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_collateral",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_feeLiquidated",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_liquidatedCollateralForFee",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "OriginationFeeLiquidated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_newStableRate",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_borrowBalanceIncrease",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "RebalanceStableBorrowRate",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "RedeemUnderlying",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_repayer",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_amountMinusFees",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_fees",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_borrowBalanceIncrease",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "Repay",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "ReserveUsedAsCollateralDisabled",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "ReserveUsedAsCollateralEnabled",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_newRateMode",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_newRate",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_borrowBalanceIncrease",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "Swap",
    "type": "event"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "LENDINGPOOL_REVISION",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "UINT_MAX_VALUE",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "addressesProvider",
    "outputs": [
      {
        "internalType": "contract LendingPoolAddressesProvider",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "core",
    "outputs": [
      {
        "internalType": "contract LendingPoolCore",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "dataProvider",
    "outputs": [
      {
        "internalType": "contract LendingPoolDataProvider",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "parametersProvider",
    "outputs": [
      {
        "internalType": "contract LendingPoolParametersProvider",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "contract LendingPoolAddressesProvider",
        "name": "_addressesProvider",
        "type": "address"
      }
    ],
    "name": "initialize",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      },
      {
        "internalType": "uint16",
        "name": "_referralCode",
        "type": "uint16"
      }
    ],
    "name": "deposit",
    "outputs": [],
    "payable": True,
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address payable",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_aTokenBalanceAfterRedeem",
        "type": "uint256"
      }
    ],
    "name": "redeemUnderlying",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_interestRateMode",
        "type": "uint256"
      },
      {
        "internalType": "uint16",
        "name": "_referralCode",
        "type": "uint16"
      }
    ],
    "name": "borrow",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      },
      {
        "internalType": "address payable",
        "name": "_onBehalfOf",
        "type": "address"
      }
    ],
    "name": "repay",
    "outputs": [],
    "payable": True,
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "swapBorrowRateMode",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "rebalanceStableBorrowRate",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "bool",
        "name": "_useAsCollateral",
        "type": "bool"
      }
    ],
    "name": "setUserUseReserveAsCollateral",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_collateral",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_purchaseAmount",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "_receiveAToken",
        "type": "bool"
      }
    ],
    "name": "liquidationCall",
    "outputs": [],
    "payable": True,
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_receiver",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      },
      {
        "internalType": "bytes",
        "name": "_params",
        "type": "bytes"
      }
    ],
    "name": "flashLoan",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveConfigurationData",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "ltv",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "liquidationThreshold",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "liquidationBonus",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "interestRateStrategyAddress",
        "type": "address"
      },
      {
        "internalType": "bool",
        "name": "usageAsCollateralEnabled",
        "type": "bool"
      },
      {
        "internalType": "bool",
        "name": "borrowingEnabled",
        "type": "bool"
      },
      {
        "internalType": "bool",
        "name": "stableBorrowRateEnabled",
        "type": "bool"
      },
      {
        "internalType": "bool",
        "name": "isActive",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveData",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "totalLiquidity",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "availableLiquidity",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "totalBorrowsStable",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "totalBorrowsVariable",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "liquidityRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "variableBorrowRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "stableBorrowRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "averageStableBorrowRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "utilizationRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "liquidityIndex",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "variableBorrowIndex",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "aTokenAddress",
        "type": "address"
      },
      {
        "internalType": "uint40",
        "name": "lastUpdateTimestamp",
        "type": "uint40"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserAccountData",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "totalLiquidityETH",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "totalCollateralETH",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "totalBorrowsETH",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "totalFeesETH",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "availableBorrowsETH",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "currentLiquidationThreshold",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "ltv",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "healthFactor",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserReserveData",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "currentATokenBalance",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "currentBorrowBalance",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "principalBorrowBalance",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "borrowRateMode",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "borrowRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "liquidityRate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "originationFee",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "variableBorrowIndex",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "lastUpdateTimestamp",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "usageAsCollateralEnabled",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getReserves",
    "outputs": [
      {
        "internalType": "address[]",
        "name": "",
        "type": "address[]"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  }
]

lending_pool_core_abi = [
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "reserve",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "liquidityRate",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "stableBorrowRate",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "variableBorrowRate",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "liquidityIndex",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "variableBorrowIndex",
        "type": "uint256"
      }
    ],
    "name": "ReserveUpdated",
    "type": "event"
  },
  {
    "payable": True,
    "stateMutability": "payable",
    "type": "fallback"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "CORE_REVISION",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "addressesProvider",
    "outputs": [
      {
        "internalType": "contract LendingPoolAddressesProvider",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "lendingPoolAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "reservesList",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "contract LendingPoolAddressesProvider",
        "name": "_addressesProvider",
        "type": "address"
      }
    ],
    "name": "initialize",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "_isFirstDeposit",
        "type": "bool"
      }
    ],
    "name": "updateStateOnDeposit",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amountRedeemed",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "_userRedeemedEverything",
        "type": "bool"
      }
    ],
    "name": "updateStateOnRedeem",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_availableLiquidityBefore",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_income",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_protocolFee",
        "type": "uint256"
      }
    ],
    "name": "updateStateOnFlashLoan",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amountBorrowed",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_borrowFee",
        "type": "uint256"
      },
      {
        "internalType": "enum CoreLibrary.InterestRateMode",
        "name": "_rateMode",
        "type": "uint8"
      }
    ],
    "name": "updateStateOnBorrow",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_paybackAmountMinusFees",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_originationFeeRepaid",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_balanceIncrease",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "_repaidWholeLoan",
        "type": "bool"
      }
    ],
    "name": "updateStateOnRepay",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_principalBorrowBalance",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_compoundedBorrowBalance",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_balanceIncrease",
        "type": "uint256"
      },
      {
        "internalType": "enum CoreLibrary.InterestRateMode",
        "name": "_currentRateMode",
        "type": "uint8"
      }
    ],
    "name": "updateStateOnSwapRate",
    "outputs": [
      {
        "internalType": "enum CoreLibrary.InterestRateMode",
        "name": "",
        "type": "uint8"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_principalReserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_collateralReserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amountToLiquidate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_collateralToLiquidate",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_feeLiquidated",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_liquidatedCollateralForFee",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_balanceIncrease",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "_liquidatorReceivesAToken",
        "type": "bool"
      }
    ],
    "name": "updateStateOnLiquidation",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_balanceIncrease",
        "type": "uint256"
      }
    ],
    "name": "updateStateOnRebalance",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "bool",
        "name": "_useAsCollateral",
        "type": "bool"
      }
    ],
    "name": "setUserUseReserveAsCollateral",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address payable",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "transferToUser",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_token",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "_destination",
        "type": "address"
      }
    ],
    "name": "transferToFeeCollectionAddress",
    "outputs": [],
    "payable": True,
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_token",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "_destination",
        "type": "address"
      }
    ],
    "name": "liquidateFee",
    "outputs": [],
    "payable": True,
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address payable",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "transferToReserve",
    "outputs": [],
    "payable": True,
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserBasicReserveData",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "isUserAllowedToBorrowAtStable",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserUnderlyingAssetBalance",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveInterestRateStrategyAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveATokenAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveAvailableLiquidity",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveTotalLiquidity",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveNormalizedIncome",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveTotalBorrows",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveTotalBorrowsStable",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveTotalBorrowsVariable",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveLiquidationThreshold",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveLiquidationBonus",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveCurrentVariableBorrowRate",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveCurrentStableBorrowRate",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveCurrentAverageStableBorrowRate",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveCurrentLiquidityRate",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveLiquidityCumulativeIndex",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveVariableBorrowsCumulativeIndex",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveConfiguration",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveDecimals",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "isReserveBorrowingEnabled",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "isReserveUsageAsCollateralEnabled",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveIsStableBorrowRateEnabled",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveIsActive",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveIsFreezed",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveLastUpdate",
    "outputs": [
      {
        "internalType": "uint40",
        "name": "timestamp",
        "type": "uint40"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "getReserveUtilizationRate",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getReserves",
    "outputs": [
      {
        "internalType": "address[]",
        "name": "",
        "type": "address[]"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "isUserUseReserveAsCollateralEnabled",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserOriginationFee",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserCurrentBorrowRateMode",
    "outputs": [
      {
        "internalType": "enum CoreLibrary.InterestRateMode",
        "name": "",
        "type": "uint8"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserCurrentStableBorrowRate",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserBorrowBalances",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserVariableBorrowCumulativeIndex",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserLastUpdate",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "timestamp",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [],
    "name": "refreshConfiguration",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_aTokenAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_decimals",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "_interestRateStrategyAddress",
        "type": "address"
      }
    ],
    "name": "initReserve",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_rateStrategyAddress",
        "type": "address"
      }
    ],
    "name": "setReserveInterestRateStrategyAddress",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "bool",
        "name": "_stableBorrowRateEnabled",
        "type": "bool"
      }
    ],
    "name": "enableBorrowingOnReserve",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "disableBorrowingOnReserve",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_baseLTVasCollateral",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_liquidationThreshold",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_liquidationBonus",
        "type": "uint256"
      }
    ],
    "name": "enableReserveAsCollateral",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "disableReserveAsCollateral",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "enableReserveStableBorrowRate",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "disableReserveStableBorrowRate",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "activateReserve",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "deactivateReserve",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "freezeReserve",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      }
    ],
    "name": "unfreezeReserve",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_ltv",
        "type": "uint256"
      }
    ],
    "name": "setReserveBaseLTVasCollateral",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_threshold",
        "type": "uint256"
      }
    ],
    "name": "setReserveLiquidationThreshold",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_bonus",
        "type": "uint256"
      }
    ],
    "name": "setReserveLiquidationBonus",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_reserve",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_decimals",
        "type": "uint256"
      }
    ],
    "name": "setReserveDecimals",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  }
]

lending_pool_addresses_provider_abi = [
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "EthereumAddressUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "FeeProviderUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "LendingPoolConfiguratorUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "LendingPoolCoreUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "LendingPoolDataProviderUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "LendingPoolLiquidationManagerUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "LendingPoolManagerUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "LendingPoolParametersProviderUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "LendingPoolUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "LendingRateOracleUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "previousOwner",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipTransferred",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "PriceOracleUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": False,
        "internalType": "bytes32",
        "name": "id",
        "type": "bytes32"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "ProxyCreated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "newAddress",
        "type": "address"
      }
    ],
    "name": "TokenDistributorUpdated",
    "type": "event"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "_key",
        "type": "bytes32"
      }
    ],
    "name": "getAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "isOwner",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "owner",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [],
    "name": "renounceOwnership",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "transferOwnership",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getLendingPool",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_pool",
        "type": "address"
      }
    ],
    "name": "setLendingPoolImpl",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getLendingPoolCore",
    "outputs": [
      {
        "internalType": "address payable",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_lendingPoolCore",
        "type": "address"
      }
    ],
    "name": "setLendingPoolCoreImpl",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getLendingPoolConfigurator",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_configurator",
        "type": "address"
      }
    ],
    "name": "setLendingPoolConfiguratorImpl",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getLendingPoolDataProvider",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_provider",
        "type": "address"
      }
    ],
    "name": "setLendingPoolDataProviderImpl",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getLendingPoolParametersProvider",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_parametersProvider",
        "type": "address"
      }
    ],
    "name": "setLendingPoolParametersProviderImpl",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getFeeProvider",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_feeProvider",
        "type": "address"
      }
    ],
    "name": "setFeeProviderImpl",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getLendingPoolLiquidationManager",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_manager",
        "type": "address"
      }
    ],
    "name": "setLendingPoolLiquidationManager",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getLendingPoolManager",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_lendingPoolManager",
        "type": "address"
      }
    ],
    "name": "setLendingPoolManager",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getPriceOracle",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_priceOracle",
        "type": "address"
      }
    ],
    "name": "setPriceOracle",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getLendingRateOracle",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_lendingRateOracle",
        "type": "address"
      }
    ],
    "name": "setLendingRateOracle",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "getTokenDistributor",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_tokenDistributor",
        "type": "address"
      }
    ],
    "name": "setTokenDistributor",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  }
]

lending_rate_oracle_abi = [
  {"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"constant":True,"inputs":[{"internalType":"address","name":"_asset","type":"address"}],"name":"getMarketBorrowRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_asset","type":"address"}],"name":"getMarketLiquidityRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_asset","type":"address"},{"internalType":"uint256","name":"_rate","type":"uint256"}],"name":"setMarketBorrowRate","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_asset","type":"address"},{"internalType":"uint256","name":"_rate","type":"uint256"}],"name":"setMarketLiquidityRate","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"}
]

interest_rate_strategy_abi = [
    {"inputs":[{"internalType":"contract LendingPoolAddressesProvider","name":"_provider","type":"address"},{"internalType":"uint256","name":"_baseVariableBorrowRate","type":"uint256"},{"internalType":"uint256","name":"_variableRateSlope1","type":"uint256"},{"internalType":"uint256","name":"_variableRateSlope2","type":"uint256"},{"internalType":"uint256","name":"_stableRateSlope1","type":"uint256"},{"internalType":"uint256","name":"_stableRateSlope2","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"constant":True,"inputs":[],"name":"OPTIMAL_UTILIZATION_RATE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"addressesProvider","outputs":[{"internalType":"contract LendingPoolAddressesProvider","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"_reserve","type":"address"},{"internalType":"uint256","name":"_availableLiquidity","type":"uint256"},{"internalType":"uint256","name":"_totalBorrowsStable","type":"uint256"},{"internalType":"uint256","name":"_totalBorrowsVariable","type":"uint256"},{"internalType":"uint256","name":"_averageStableBorrowRate","type":"uint256"}],"name":"calculateInterestRates","outputs":[{"internalType":"uint256","name":"currentLiquidityRate","type":"uint256"},{"internalType":"uint256","name":"currentStableBorrowRate","type":"uint256"},{"internalType":"uint256","name":"currentVariableBorrowRate","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"getBaseVariableBorrowRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"getStableRateSlope1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"getStableRateSlope2","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"getVariableRateSlope1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"getVariableRateSlope2","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}
]

token_abi = [
  {"constant":False,"inputs":[{"name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"newImplementation","type":"address"},{"name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"implementation","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"newAdmin","type":"address"}],"name":"changeAdmin","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"admin","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_implementation","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"anonymous":False,"inputs":[{"indexed":False,"name":"previousAdmin","type":"address"},{"indexed":False,"name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"name":"implementation","type":"address"}],"name":"Upgraded","type":"event"}
]

a_token_abi = [
  {
    "inputs": [
      {
        "internalType": "contract LendingPoolAddressesProvider",
        "name": "_addressesProvider",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_underlyingAsset",
        "type": "address"
      },
      {
        "internalType": "uint8",
        "name": "_underlyingAssetDecimals",
        "type": "uint8"
      },
      {
        "internalType": "string",
        "name": "_name",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "_symbol",
        "type": "string"
      }
    ],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_from",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_to",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_fromBalanceIncrease",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_toBalanceIncrease",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_fromIndex",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_toIndex",
        "type": "uint256"
      }
    ],
    "name": "BalanceTransfer",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_from",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_fromBalanceIncrease",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_fromIndex",
        "type": "uint256"
      }
    ],
    "name": "BurnOnLiquidation",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_from",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_to",
        "type": "address"
      }
    ],
    "name": "InterestRedirectionAllowanceChanged",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_from",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_to",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_redirectedBalance",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_fromBalanceIncrease",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_fromIndex",
        "type": "uint256"
      }
    ],
    "name": "InterestStreamRedirected",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_from",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_fromBalanceIncrease",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_fromIndex",
        "type": "uint256"
      }
    ],
    "name": "MintOnDeposit",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_from",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_fromBalanceIncrease",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_fromIndex",
        "type": "uint256"
      }
    ],
    "name": "Redeem",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_targetAddress",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_targetBalanceIncrease",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_targetIndex",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_redirectedBalanceAdded",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_redirectedBalanceRemoved",
        "type": "uint256"
      }
    ],
    "name": "RedirectedBalanceUpdated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
    "type": "event"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "UINT_MAX_VALUE",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "spender",
        "type": "address"
      }
    ],
    "name": "allowance",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "decimals",
    "outputs": [
      {
        "internalType": "uint8",
        "name": "",
        "type": "uint8"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "subtractedValue",
        "type": "uint256"
      }
    ],
    "name": "decreaseAllowance",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "addedValue",
        "type": "uint256"
      }
    ],
    "name": "increaseAllowance",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "name",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "symbol",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "recipient",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "transfer",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "sender",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "recipient",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "transferFrom",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "underlyingAssetAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_to",
        "type": "address"
      }
    ],
    "name": "redirectInterestStream",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_from",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_to",
        "type": "address"
      }
    ],
    "name": "redirectInterestStreamOf",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_to",
        "type": "address"
      }
    ],
    "name": "allowInterestRedirectionTo",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "redeem",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_account",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "mintOnDeposit",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_account",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "burnOnLiquidation",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "internalType": "address",
        "name": "_from",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "transferOnLiquidation",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "principalBalanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "totalSupply",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "isTransferAllowed",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserIndex",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getInterestRedirectionAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getRedirectedBalance",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  }
]