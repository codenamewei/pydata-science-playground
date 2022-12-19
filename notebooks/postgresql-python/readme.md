
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
