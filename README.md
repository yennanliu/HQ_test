# HQ_test


```

DB :

+--------------------+
| Database           |
+--------------------+
| information_schema |
| HQ_test            |
| bi_data            |
| mysql              |
| pcmDB              |
| performance_schema |
| primary_data       |
| sys                |
+--------------------+


table :

+------------------------+
| Tables_in_primary_data |
+------------------------+
| fx_rate                |
| lst_currency           |
| offer                  |
+------------------------+


+-------------------+
| Tables_in_bi_data |
+-------------------+
| hotel_offers      |
| valid_offers      |
+-------------------+


```

Setting up :

step 1 : install MySQL :

```
$ sudo yum install mysql-server
```

step 2 : launch MySQL server :

```
$ mysql.server start
```

step 3 : clone the repo :

```
$ git clone https://github.com/yennanliu/HQ_test

```


