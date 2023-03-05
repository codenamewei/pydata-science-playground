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
- Commit as you go style:
   - queries not committed unless call explicitly
   - Alternatively, can set autocommit = True
   - There is also another style of committing data, which is that we can declare our “connect” block to be a transaction block up front. Check more in [1_getting_a_connection.ipynb](1_getting_a_connection.ipynb)
   - Connection-based method: `engine` -> `connection.execute()` with object `text()`
        
### Keywords

- **Engine**
  ```
  Establish Connectivitity. This should be a global param declare only one time
  ```
- **Session**
  ```
   One of the core concepts in SQLAlchemy is the Session . A Session establishes and maintains all conversations between your program and the databases. It represents an intermediary zone for all the Python model objects you have loaded in it
  ```
- **Result**
  - `Result.all()`: return a list of all Row objects (iterable)
    - Row object can be access in a few methods
        - Tuple assignment
          ```
          result = conn.execute(text("select x, y from some_table"))

          for x, y in result:
          ```
        - Integer Index
          ```
          result = conn.execute(text("select x, y from some_table"))

          for row in result:
            x = row[0]
          ```
        - Named Tuple
          ```
          result = conn.execute(text("select x, y from some_table"))

          for row in result:
            y = row.y

            # illustrate use with Python f-strings
            print(f"Row: {row.x} {y}")
          ```
        - Mapping Access using Result.mapping()
            - this returns RowMapping object rather than Row objects
              ```
              result = conn.execute(text("select x, y from some_table"))

              for dict_row in result.mappings():
                    x = dict_row["x"]
                    y = dict_row["y"
              ```
 - **Metadata**
     - Having a single MetaData object for an entire application is the most common case
     - There can be multiple MetaData collections as well; Table objects can refer to Table objects in other collections without restrictions. However, for groups of Table objects that are related to each other, it is in practice much more straightforward to have them set up within a single MetaData collection
- **Table**: database table
- **Column**: 
    - a column in database table
    - usually includes a string name and a type object
    - The collection of Column are normally accessed with `Table.c`
        - Get particular column (example: name): `user_table.c.name`
            - Column('name', String(length=30), table=<user_account>)
        - Get list of column names: `user_table.c.keys()`
            - ['id', 'name', 'fullname']
        - Get primary key: `user_table.primary_key`
        - Declare foreign key
            - Example: a second table address that will have a foreign key constraint referring to the user table
            - When using the ForeignKey object within a Column definition, we can omit the datatype for that Column; it is automatically inferred from that of the related column
              ```
               from sqlalchemy import ForeignKey
               address_table = Table(
                    "address",
                    metadata_obj,
                    Column("id", Integer, primary_key=True),
                    Column("user_id", ForeignKey("user_account.id"), nullable=False),
                    Column("email_address", String, nullable=False),
               )
              ```
         - Null constraint with: `nullable=True/False`
         - Create table with: `metadata_obj.create_all(engine)`
         - [Drop table with:](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.MetaData.drop_all) `metadata_obj.drop_all()`
         - Indicate column with: `mapped_column()`with typing annotation `Mapped` type
             - `id: Mapped[int] = mapped_column(primary_key=True)`
             - `user_id= mapped_column(ForeignKey("user_account.id"))` (Typing annotation can choose to be omitted because its declared elsewhere)
             - `email_addresss: Mapped[str]`: Only declare typing annotation when there are no further info to add
- **Data Definition Language (DDL) 
    - An acronym for Data Definition Language. DDL is the subset of SQL that relational databases use to configure tables, constraints, and other permanent objects within a database schema. SQLAlchemy provides a rich API for constructing and emitting DDL expressions.


### More to read
- [Table Configuration with Declarative](https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#orm-declarative-mapped-column)
- [Working with Related Objects](https://docs.sqlalchemy.org/en/20/tutorial/orm_related_objects.html#tutorial-orm-related-objects)
- [ORM Declarative Native Dataclasses](https://docs.sqlalchemy.org/en/20/orm/dataclasses.html#orm-declarative-native-dataclasses)



### References
- **[SQL Alchemy Tutorial](https://docs.sqlalchemy.org/en/20/)**
- https://dev.to/spaceofmiah/sqlalchemy-hello-world-3aif
- https://www.geeksforgeeks.org/how-to-update-sqlalchemy-row-entry/
- https://4geeks.com/lesson/everything-you-need-to-start-using-sqlalchemy
