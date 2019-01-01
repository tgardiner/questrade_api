# questrade_api
Python3 Questrade API Wrapper

## Installation
* Use `pip`/`pip3`:

   `pip3 install questrade-api`

## Getting Started
1. Familiarise yourself with the [Security documentation](https://www.questrade.com/api/documentation/security) for the Questrade API.
2. [Generate](https://login.questrade.com/APIAccess/UserApps.aspx) a manual refresh token for your application.
3. Init the API Wrapper with the refresh token:

   ```
   from questrade_api import Questrade
   q = Questrade(refresh_token='XYz1dBlop33lLLuys4Bd')
   ```
   **Important:**
   A token will be created at `~/.questrade.json` and used for future API calls
   * If the token is valid future initiations will not require a refresh token

   ```
   from questrade_api import Questrade
   q = Questrade()
   ```

---

## Using the API
### [Time](https://www.questrade.com/api/documentation/rest-operations/account-calls/time)

```
q.time
=> {'time': '2018-11-16T09:22:27.090000-05:00'}
```

### [Accounts](https://www.questrade.com/api/documentation/rest-operations/account-calls/accounts)

```
q.accounts
=> {'accounts': [{'type': 'Margin', 'number': '123456', 'status': 'Active' ...}]}
```

### [Account Positions](https://www.questrade.com/api/documentation/rest-operations/account-calls/accounts-id-positions)

Accepts: `<account_id>`

```
q.account_positions(123456)
=> {'positions': [{'symbol': 'RY.TO', 'symbolId': 34658, 'openQuantity': ...}]}
```

### [Account Balances](https://www.questrade.com/api/documentation/rest-operations/account-calls/accounts-id-balances)

Accepts: `<account_id>`

```
q.account_balances(123456)
=> {'perCurrencyBalances': [{'currency': 'CAD', 'cash': 1000, 'marketValue': 0, ...}]}
```

### [Account Executions](https://www.questrade.com/api/documentation/rest-operations/account-calls/accounts-id-executions)

Accepts: `<account_id>`, `startTime=`, `endTime=`

```
q.account_executions(123456)
=> {'executions': []}
```

```
q.account_executions(123456,startTime='2018-08-01T00:00:00-0')
=> {'executions': [{'symbol': 'RY.TO', 'symbolId': 34658, 'quantity': 100, ...}]}
```

### [Account Orders](https://www.questrade.com/api/documentation/rest-operations/account-calls/accounts-id-orders)

Accepts: `<account_id>`, `startTime=`, `endTime=`, `stateFilter=`

```
q.account_orders(123456)
=> {'orders': []}
```

```
q.account_orders(123456, startTime='2018-08-01T00:00:00-0')
=> {'orders': [{'id': 444444, 'symbol': 'RY.TO', 'symbolId': 34658, ...}]}
```

### [Account Order](https://www.questrade.com/api/documentation/rest-operations/account-calls/accounts-id-orders)

Accepts: `<account_id>`, `<order_id>`

```
q.account_order(123456, 444444)
=> {'orders': [{'id': 444444, 'symbol': 'RY.TO', 'symbolId': 34658, 'totalQuantity': 100, ...}]}
```

### [Account Activities](https://www.questrade.com/api/documentation/rest-operations/account-calls/accounts-id-activities)

Accepts: `<account_id>`, `startTime=`, `endTime=`

```
q.account_activities(123456)
=> {'activities': []}
```

```
q.account_activities(123456, startTime='2018-11-01T00:00:00-0')
=> {'activities': []}
```

### [Symbol](https://www.questrade.com/api/documentation/rest-operations/market-calls/symbols-id)

Accepts: `<symbol_id>`

```
q.symbol(34659)
=> {'symbols': [{'symbol': 'RY.TO 'symbolId': 34658, 'prevDayClosePrice': ...}]}
```

### [Symbols](https://www.questrade.com/api/documentation/rest-operations/market-calls/symbols-id)

Accepts: `ids='<symbol_id_1>,<symbol_id_2>'`, `names='<symbol_1>,<symbol_2>'`

```
q.symbols(ids='34658,9339')
=> {'symbols': [{'symbol': 'RY.TO', 'symbolId': 34658, 'prevDayClosePrice': ..}]}
```

```
q.symbols(names='RY.TO,BNS.TO')
=> {'symbols': [{'symbol': 'RY.TO', 'symbolId': 34658, 'prevDayClosePrice': ..}]}
```

### [Symbols Search](https://www.questrade.com/api/documentation/rest-operations/market-calls/symbols-search)

Accepts: `prefix='<symbol_1>'`, `offset=`

```
q.symbols_search(prefix='RY.TO')
=> {'symbols': [{'symbol': 'RY.TO', 'symbolId': 34658, 'description': ...}]}
```

```
q.symbols_search(prefix='RY', offset=5)
{'symbols': [{'symbol': 'RY.PRE.TO', 'symbolId': 34700, 'description': ...}]}
```

### [Symbol Options](https://www.questrade.com/api/documentation/rest-operations/market-calls/symbols-id-options)

Accepts: `<symbol_id>`

```
q.symbol_options(34658)
=> {'optionChain': [{'expiryDate': '2018-11-16T00:00:00.000000-05:00', 'description': ... }]}
```

### [Markets](https://www.questrade.com/api/documentation/rest-operations/market-calls/markets)

```
q.markets
=> {'markets': [{'name': 'TSX', 'tradingVenues': ['TSX', 'ALPH', 'CXC', ... }]}
```

### [Markets Quote](https://www.questrade.com/api/documentation/rest-operations/market-calls/markets-quotes-id)

Accepts: `<symbol_id>`

```
q.markets_quote(34658)
=> {'quotes': [{'symbol': 'RY.TO', 'symbolId': 34658, 'tier': ... }]}
```

### [Markets Quotes](https://www.questrade.com/api/documentation/rest-operations/market-calls/markets-quotes-id)

Accepts: `ids='<symbol_id_1>,<symbol_id_2>'`

```
q.markets_quotes(ids='34658,9339')
=> {'quotes': [{'symbol': 'RY.TO', 'symbolId': 34658, 'tier': ... }]}
```

### [Markets Options](https://www.questrade.com/api/documentation/rest-operations/market-calls/markets-quotes-options)

Accepts: `optionIds=`, `filters=`

```
q.markets_options(optionIds=[
    23615873,
    23615874
])
=> {'optionQuotes': [{'underlying': 'RY.TO', 'underlyingId': 34658, 'symbol': 'RY30Nov18 ..}]}
```

```
q.markets_options(filters=[
    {
        "optionType": "Call",
        "underlyingId": 34658,
        "expiryDate": "2018-11-30T00:00:00.000000-05:00",
        "minstrikePrice": 90,
        "maxstrikePrice": 100
    }
])
=> {'optionQuotes': [{'underlying': 'RY.TO', 'underlyingId': 34658, 'symbol': 'RY30Nov18 ..}]}
```

### [Markets Strategies](https://www.questrade.com/api/documentation/rest-operations/market-calls/markets-quotes-strategies)

Accepts: `variants=`

```
q.markets_strategies(variants=[
    {
        "variantId": 1,
        "strategy": "Custom",
        "legs": [
            {
                    "symbolId": 23545340,
                    "ratio": 10,
                    "action": "Buy"
            },
            {
                "symbolId": 23008592,
                "ratio": 10,
                "action": "Sell"
            }
        ]
    }
])
=> {'strategyQuotes': [{'variantId': 1, 'bidPrice': None, 'askPrice': None, 'underlying': 'RY.TO' ...}]}
```

### [Markets Candles](https://www.questrade.com/api/documentation/rest-operations/market-calls/markets-candles-id)

Accepts: `<symbol_id>`, `startTime=`, `endTime=`, `interval=`

```
q.markets_candles(34658, interval='FiveMinutes')
=> {'candles': [{'start': '2018-11-16T09:30:00.583000-05:00', 'end': '2018-11-16T ..}]}
```
