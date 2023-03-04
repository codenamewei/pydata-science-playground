- if commit() is not called, the effect of any data manipulation will be lost.
  Alternatively, set `autocommit` mode
- `cursor.rollback()`
    - It restores the database to last your last COMMIT. You can also use it with SAVEPOINT command to jump to a savepoint in a ongoing transaction.
    - works when autocommit != True