## Difference of psycopg2 and psycopg3

- Psycopg 3 is a complete rewrite of Psycopg 2, maintaining the same fundamental libpq wrapper architecture and DB-API interface design, but exposing new features to better work with the newer versions of Python and PostgreSQL.
- Example of features of Psycopg 3 (compared to psycopg2)
  - use of asyncio-based concurrency
  - static typing

## Install psycopg3

### Create the environment
```
conda env create -f config_psycopg3.yml
```

### Activate the environment
```
conda activate postgres3-playground
```

Run
```
pip install --pre psycopg[binary,pool]  # install binary files
```

## Commands 
- connect to database
  ```
  try:
    conn = psycopg.connect(
        user="postgres",
        password="password",
        host="database.cosqamqjez6h.ap-northeast-2.rds.amazonaws.com",
        port='5432'
    )

   except:
    raise Exception("Failed to connect to database")
  ```
  - PostgreSQL does not have an autocommit facility which means that all queries will execute within a transaction. 
    To make transaction on every query. Put `autocommit = True` in connection
    ```
    conn = psycopg.connect(
        ...,
        autocommit = True
    )
    ```
- get a cursor to perform database operations
  ```cur = conn.cursor()```
- execute a command: for operations such as CREATE, INSERT INTO  
  ```cur.execute(<command>)```
  To handle exception: 
  ```
  try:
    cur.execute(<command>)
  except:
    raise Exception("Failed to execute command")
  ```
- get data: for operations such as SELECT
  - ```cur.fetchone()```  
  - ```cur.fetchmany(n)```
  - ```cur.fetchall()```: return a list


## Other Notes

- [How to drop DATABASE](https://wiki.postgresql.org/wiki/Psycopg2_Tutorial)
