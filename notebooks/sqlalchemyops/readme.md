- For Object Relational Mapping, use SQLAlchemy to connect to database
  ```
    Firebird
    Microsoft SQL Server
    MySQL
    Oracle
    PostgreSQL
    SQLite
    Sybase
  ```
- Install ```pip install sqlalchemy``` 
- SQLAlchemy matches Python data to the best possible generic column data types defined in it. Some of the generic data types are −
  ```
    BigInteger
    Boolean
    Date
    DateTime
    Float
    Integer
    Numeric
    SmallInteger
    String
    Text
    Time
   ```
- There's a need to install database driver for the database to connect 
  `db+driver://user:password@host/dbname`
  Example:
  ```
  mysql+pymysql://<username>:<password>@<host>/<dbname>
  postgresql+psycopg://{db_username}:{db_password}@{db_host}:{db_port}
  ```
- SQLAlchemy is presented as two distinct APIs.
  - **Core**
  - **ORM** (ORM building on top of Core for **object relational mapping** capabilities
    - This includes
        - additional configuration layer to map user-defined Python classes to database tables
        - object persistence mechanism as **Session**
        - also extends Core to perform queries
- What is Session?
  ```
  ```


### References
- **[SQL Alchemy Tutorial](https://docs.sqlalchemy.org/en/20/)**
- https://dev.to/spaceofmiah/sqlalchemy-hello-world-3aif
- https://www.geeksforgeeks.org/how-to-update-sqlalchemy-row-entry/
- https://4geeks.com/lesson/everything-you-need-to-start-using-sqlalchemy
