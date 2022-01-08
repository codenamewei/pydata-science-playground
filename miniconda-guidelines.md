# [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

**Conda create an environment specifying python version**
```
conda create -n myenv python=3.8.5
```

**Conda create an environment from yml file**
```
conda env create -f config.yml
```

**Conda create yml file from an existing environment**
```
conda env export --file config.yml
```

**Install a package with version**
```
conda install package=20.0.0
```
**Install package with yes**
```
conda install package -y
```

**Uninstall/remove a package**
_Note: Outside of an environment_
```
conda remove -n myenv scipy
```

_Note: In an environment_
```
conda remove scipy
```

_Alias of conda remove is conda uninstall_


**Conda activate an environment**
```
conda activate python-dev-env
```

**Conda deactivate an environment**
```
conda deactivate
```

**Conda list all environments available**
```
conda env list
```

**Conda list all packages in an environment**
```
conda list -n python-dev-env
```

**Conda remove environment**
```
conda env remove --name python-dev-env
```
**Conda update environment**
**According to the changes of the configuration file**
```
conda env update --prefix /home/codenamewei/miniconda3/envs/python-dev-env --file environment.yml --prune
```
_Note: prefix is the full path to the environment location_

**Rebuild environment forcefully**
```
conda env create --prefix /home/codenamewei/miniconda3/envs/python-dev-env --file environment.yml --force
```

**Conda export environment**
```
conda env export > environment.yml
```
```
name: python-dev-env
channels:
  - pytorch
dependencies:
  - argon2-cffi=20.1.0=py38h7b6447c_1
 prefix: /home/codenamewei/miniconda3/envs/python-dev-env
```

**_config.yml_ Skeleton Structure**
```
name: python-dev-env
channels:
  - anaconda
dependencies:
  - python=3.7
  - pip=20.2.*
  - jupyterlab
  - pip:
    - click==7.1.*
```
#### Conda installation in ubuntu

##### Download file
1. Find the right distribution in https://repo.anaconda.com/archive/
```
wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh
```

2. Make the file executable
```
chmod +x Anaconda3-5.3.1-Linux-x86_64.sh
```

3. Select installation path
![anaconda3](https://user-images.githubusercontent.com/33477318/131203388-e7f5e47d-7072-447b-b1fb-e187716452fa.png)

