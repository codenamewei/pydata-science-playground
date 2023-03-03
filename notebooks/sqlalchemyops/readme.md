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
- if commit() is not called, the effect of any data manipulation will be lost.
  Alternatively, set `autocommit` mode
- `cursor.rollback()`
    - It restores the database to last your last COMMIT. You can also use it with SAVEPOINT command to jump to a savepoint in a ongoing transaction.
    - works when autocommit != True

### References
- https://dev.to/spaceofmiah/sqlalchemy-hello-world-3aif
- https://www.geeksforgeeks.org/how-to-update-sqlalchemy-row-entry/
- https://docs-sqlalchemy.readthedocs.io/ko/latest/core/connections.html
- https://4geeks.com/lesson/everything-you-need-to-start-using-sqlalchemy