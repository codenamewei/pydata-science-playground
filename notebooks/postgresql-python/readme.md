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
