# Snippets of Code for Data Science Operations in Python



<div align="center">
  <img alt="datascienceplaygronud" src="metadata/pydatascienceplayground.png"><br>
</div>

<p>
  <p align="left">
<img alt="project status: active" src="https://img.shields.io/badge/Project%20Status-%F0%9F%94%A5Active-brightgreen"> 

</p>



# Environment Setup
```
cd <path-to>/data-science-playground
conda env create -f config.yml
```

# Gist 

## [Pandas](https://pandas.pydata.org/docs/reference/)

### Infos
- [Dataframe basic](notebooks/pandas/info_basic.ipynb)
    - Get # rows and columns
    - Get summary/infos about dataframe
= [Get data types](notebooks/pandas/column_types.ipynb)
- [Dataframe/Series Min, Max, Median, General Description](notebooks/pandas/series_min_max.ipynb)
- [Get rows name (index) and columns name (column)](notebooks/pandas/info_rows_columns.ipynb)
- [Get a glimpse of dataframe](notebooks/pandas/info_glimpse.ipynb)
- [Get subset of a dataframe by rows/by columns](notebooks/pandas/df_subset.ipynb)
- [Get rows by finding matching values from a specific column](notebooks/pandas/df_find_rows.ipynb)
- Check if a column name exist in dataframe - ```if 'code' in df.columns:```
- [Iteration of each rows in a dataframe](notebooks/pandas/iterrows.ipynb)

### Operations
- [Get dataframe from list](notebooks/pandas/list2df.ipynb)
- [Get subset of dataframe, sample columns with specific criteria](notebooks/pandas/sample_df.ipynb)
    - Sample by percentage
    - Sample by # of rows specified
    - Sample by matching to a value
- Column to list: [```df['sample_column'].tolist()```](notebooks/pandas/columns2list.ipynb)  
- Sample rows: ```df = df.sample(frac=1).reset_index(drop=True) ```
- [Referring to dataframe column by key or by string](notebooks/pandas/refer_column_name.ipynb)
- [Concatenate dataframe](notebooks/pandas/concat_df.ipynb)
    - Concatenate by adding rows
- [Append string to all rows of a column](notebooks/pandas/append_value_to_rows.ipynb)
- Reset index without creating new (index) column - ```df.reset_index(drop=True)```
- Assign df by copy instead of reference - [```df.copy()```](notebooks/pandas/copybyvalue.ipynb)

### Type
- [Series to value](notebooks/pandas/series_to_values.ipynb)
- Series to numpy array - ```input.to_numpy()```
- [Change column type](notebooks/pandas/change_column_type.ipynb)
- [Rename column name if exist](notebooks/pandas/rename_column.ipynb)
- [Compare column type](notebooks/pandas/comparecoltype.ipynb)

### Assign values
- [Create new column and assign value according to another column](notebooks/pandas/assign_column.ipynb)
- [Dataframe append rows](notebooks/pandas/df_append_rows.ipynb)
- Assign values by lambda - [tbd]( https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html)

### Remove/drop values
- [Drop duplicates for df / subset, keep one copy and remove all](notebooks/pandas/drop_duplicate.ipynb)
- [Remove/drop rows where specific column matched value](notebooks/pandas/remove_with_matching_value.ipynb)
- [Remove specific columns with column name](notebooks/pandas/remove_column.ipynb)
- Drop rows/columns with np.NaN: ```df3 = df3.dropna(axis = 0) #column```

### Excel like functions
- pivot table - tbd


### Maths
- [Exclude Outliers](notebooks/pandas/excludeoutliers.ipynb)

### Filtering
- [Filter with function isin()](notebooks/pandas/isin.ipynb)
- [Filter df with item not in list](notebooks/pandas/filtervaluenotinlist.ipynb)
- [Filter with function query()](notebooks/pandas/query.ipynb)
- Find with loc - ```df.loc[df['address'].eq('johndoe@gmail.com')]``` ```df.loc[df.a.eq(123) & df.b.eq("helloworld")]```
- [Assign value to specific column(s) by matching value](notebooks/pandas/df_assign_col_values.ipynb)
- Get a subset of dataframe by rows - ```df.iloc[<from_rows>:<to_rows>, :]```
- [Count items and filter by counter values](notebooks/pandas/filter&valuecount.ipynb)
- [Retrieve columns name which match specific str](notebooks/pandas/filterbysubsetname.ipynb)

### CSV In/Out
- Read csv with other delimiter ```pd.read_csv(<path-to-file>, delimiter = '\x01')```
- Read csv with bad lines ```pd.read_csv(<path-to-file>, on_bad_lines='skip')```
  - Note: ```pd.read_csv(<path>, error_bad_lines = False)``` deprecated
- Read csv with encoding ```pd.read_csv('file name', encoding = 'utf-8')```
- Save to csv ```df.to_csv('file name', index = False)```
  - Note: Put ```index = False``` is important to prevent an extra column of index being saved.
- Save to csv with encoding ```df.to_csv('file name', encoding = 'utf-8')```

### Excel In/Out
- Read in excel with specific sheet name: ```pd.read_excel(<url>, sheet_name = "Sheet1", engine = "openpyxl")```
  - Note: Install engine by ```pip install openpyxl```
- Save excel: ```df.to_excel('file_name', index = False) ```

### Pickle In/Out 
**Note: Pickle have security risk and slow in serialization (even to csv and json). Dont use**
- Read in pickle to dataframe: ```df = pd.read_pickle(<file_name>) # ends with .pkl```
- Save to pickle: ```df.to_pickle(<file_name>)```

## Numpy
- Numpy NaN (Not A Number): Constant to act as a placeholder for any missing numerical values in the array: ```np.NaN / np.nan / np.NAN```
- [Numpy <> Binary File(.npy)](notebooks/numpy/np2binary.ipynb)
- [Numpy <> Bytes](notebooks/numpy/np2bytes.ipynb)

## Pytorch
- Given torch.tensor ```buffer = tensor(4)```, get the value by - ```id = buffer.item()```
- Given torch.tensor, get the argmax of each row - ```torch.argmax(buffer, dim=<(int)dimension_to_reduce>)```
- Check if cuda is available - ```import torch; torch.cuda.is_available()``` 

## Huggingface

- Send model to cuda - ```model = model.to('cuda:0')```
- [Overview of DatasetDict](notebooks/huggingface/DatasetDict_Overview.ipynb)

## Audio 
- [Audio of .wav -> .flac](notebooks/audio/wav2flac.ipynb)
- [Get sampling rate of an audio file](notebooks/audio/getsamplingrate.ipynb)
- [Audio file <> Numpy Array](notebooks/audio/audiofile2array.ipynb)
## Input

- [Get system input](notebooks/input/sysinput.py)

## Formatting
- datetime:  [datetime.ipynb](notebooks/formatting/datetime.ipynb)

## Data Structure 

### List 
- List of str to int: ```list(map(int, arr))```
- Split str to list of str: ```arr.split(" ")```
- Sort an array in place: ```arr.sort()``` / Return a sorted array: ```sorted(arr)```
- Get index of a value: ```arr.index(value)```
- Add one more value to existing list: ```arr.append(value)```
- Extend list with values in another list: ```arr.extend(arr2)```
- Check for empty list: ```arr = []; if not arr: #empty list```

### Dictionary
- Get keys as list: ```list(lut.keys())```
- Get values as list: ```list(lut.values())```
- Create dict from list: ```{i: 0 for i in arr}```
- Find if key exists in existing dict: ```if k in lut```
- Save/load dictionary to/from a file: [saveloaddict.ipynb](notebooks/dictionary/saveloaddict.ipynb)

## Math
- [Define Nan, Infinite](notebooks/math/define_nan_infinite.ipynb)
- Sum up an array: ```sum(arr)```
- Round up a number to a certain decimal point: ```round(value, 1)``` 

## File System
- The character used by the operating system to separate pathname components: ```os.sep```
- [Iterate through a path to get files/folders of all the subpaths](notebooks/filesystem/filewalk.ipynb)
- Check if path is a folder: ```os.path.isdir(<path>)```
- Create folder: ```os.mkdir(<path>```
- Create folders recursively: ```os.makedirs(<path>)```
- Get home directory: ```os.path.expanduser('~')```
- Get current running script path: ```os.getcwd()```
- Get current file path (getcwd will point to the running script(main) path, this will get individually py path): ```os.path.dirname(os.path.abspath(__file__))```
- Append certain path: ```sys.path.append(<path>)```
- Check if path exist: ```os.path.exists(<path>)```
- Remove a file: ```os.remove()```
- Removes an empty directory: ```os.rmdir()```
- Deletes a directory and all its contents: ```shutil.rmtree()```
- [Copy a file to another path](notebooks/filesystem/copyfile.ipynb)
- [Unzip file](notebooks/filesystem/uncompresszip.ipynb)

## String
- Check file extension: [string/check_file_extension.ipynb](notebooks/string/check_file_extension.ipynb)
- Capitalize a string: ```strvar.capitalize()```
- Split a string based on character: ```strvar.split(<char>)```
  - Note: if split with every character, do this instead: ```[i for i in "ABCDE"]```
- Check if string ends with a substring: ```strvar.endswith(<substring>)```
- Check if string have substring/specific character. Returns -1 if not found. : ```strvar.find(<substring>)```
- String get substring with index: ```str[startindex:endindex]```
- Replace string/character with intended string/character: ```strout = strin.replace(" ", "_")```
- [Replace multiple string/characters with intended string/character](notebooks/string/replace_multiple_character.ipynb)

## ConfigParser
- Read from config file: [configparser/testconfig.ipynb](notebooks/configparser/testconfig.ipynb)

## URL
- [Download URL to local file](url/downloadurl.ipynb)

## Logging 
### Built-In Logging
- Basic: 
  ```
  import logging
  logger = logging.getLogger(__name__)
  logging.basicConfig(stream=sys.stdout, level=logging.INFO)
  ```
- [Advanced configuration log to stdout](notebooks/logging/builtinlogging/log2stdout.ipynb)
- [Advanced configuration log to file](notebooks/logging/builtinlogging/log2file.ipynb)

### Ice cream

- [Logging walkthrough](notebooks/logging/icecream/summary.ipynb)


## Medium Posts
- [Ctrl + c, Ctrl + v — Replicating Data Science Conda Environment](https://codenamewei.medium.com/ctrl-c-ctrl-v-replicating-data-science-conda-environment-c190ad0d93fd)
  - [Conda Commands Cheatsheet](miniconda-guidelines.md)
- [Displaying visuals with Markdown](https://medium.com/geekculture/displaying-visuals-with-markdown-c39f2495e146)
  - [Examples of displaying image in readme.md](https://github.com/codenamewei/pydata-science-playground/blob/main/notebooks/markdown/readme.md)
  - [Examples of displaying image in Jupyter](https://github.com/codenamewei/pydata-science-playground/blob/main/notebooks/markdown/markdown_guidelines.ipynb) 

