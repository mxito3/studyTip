# 带token压测并带token
```shell
ab -n 100 -c 50 -v 4 -H 'exchange-token:edcc07027dc46d7d8aaceb61bbe91097a37f6372b1894095a7680f216d0de43b' -H 'exchange-client:h5' http://127.0.0.1:8000/trade/get_limit_symbol_balance/
```