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
- [Get data types](notebooks/pandas/column_types.ipynb)
- [Dataframe/Series Min, Max, Median, General Description](notebooks/pandas/series_min_max.ipynb)
- [Get rows name (index) and columns name (column)](notebooks/pandas/info_rows_columns.ipynb)
- [Get a glimpse of dataframe](notebooks/pandas/info_glimpse.ipynb)
- [Get subset of a dataframe by rows/by columns](notebooks/pandas/df_subset.ipynb)
- [Get rows by finding matching values from a specific column](notebooks/pandas/df_find_rows.ipynb)
- Check if a column name exist in dataframe - `if 'code' in df.columns:`
- [Iteration of each rows in a dataframe](notebooks/pandas/iterrows.ipynb)

### Operations

- Check if dataframe is empty - `df.empty #return boolean`
- [Get dataframe from list](notebooks/pandas/list2df.ipynb)
- Build dataframe with columns name - `column_list = ["a", "b"] df = pd.DataFrame(columns = column_list)`
- [Build a new dataframe from a subset of columns from another dataframe](notebooks/pandas/series_subset.ipynb)
- [Get subset of dataframe, sample columns with specific criteria](notebooks/pandas/sample_df.ipynb)
  - Sample by percentage
  - Sample by # of rows specified
  - Sample by matching to a value
- Column to list: [`df.columns.tolist()`](notebooks/pandas/columns2list.ipynb)
- Sample rows: `df = df.sample(frac=1).reset_index(drop=True) `
- [Referring to dataframe column by key or by string](notebooks/pandas/refer_column_name.ipynb)
- [Concatenate dataframe](notebooks/pandas/concat_df.ipynb)
  - Concatenate by adding rows
- [Append string to all rows of a column](notebooks/pandas/append_value_to_rows.ipynb)
- Reset index without creating new (index) column - `df.reset_index(drop=True)`
- Assign df by copy instead of reference - [`df.copy()`](notebooks/pandas/copybyvalue.ipynb)
- Shuffle rows of df: `df = df.sample(frac=1).reset_index(drop=True)`
- [Pandas with multiple index](notebooks/pandas/pd_multiple_index.ipynb)

### Type

- [Change column type](notebooks/pandas/change_column_type.ipynb)
- [Rename column name if exist](notebooks/pandas/rename_column.ipynb)
- [Compare column type](notebooks/pandas/comparecoltype.ipynb)

### Series

- [Series to value](notebooks/pandas/series_to_values.ipynb)
- Series/Dataframe to numpy array - `input.to_numpy()`
- Series iteration: `for index, item in seriesf.items():`

### Assign values

- [Create new column and assign value according to another column](notebooks/pandas/assign_column.ipynb)
- [Assign values by lambda and df.assign](notebooks/pandas/dfassign.ipynb)
- [Dataframe append rows](notebooks/pandas/df_append_rows.ipynb)

### Remove/drop values

- [Drop duplicates for df / subset, keep one copy and remove all](notebooks/pandas/drop_duplicate.ipynb)
- [Remove/drop rows where specific column matched value](notebooks/pandas/remove_with_matching_value.ipynb)
- [Remove specific columns with column name](notebooks/pandas/remove_column.ipynb)
- [Drop rows by index](notebooks/pandas/drop_row_by_index.ipynb)
- Drop rows/columns with np.NaN: `df3 = df3.dropna(axis = 1) #row`

### SQL-like functions

- pivot table - tbd
  - Drawback: Not able to do filtering selection
- [Merge two dataframes based on certain column values](notebooks/pandas/pdmerge.ipynb)

### Filtering

- [Filter with function isin()](notebooks/pandas/isin.ipynb)
- [Filter df with item not in list](notebooks/pandas/filtervaluenotinlist.ipynb)
- [Filter with function query()](notebooks/pandas/query.ipynb)
- Find with loc
  - `df.loc[df['address'].eq('johndoe@gmail.com')] #filter with one value`
  - `df.loc[df.a.eq(123) & df.b.eq("helloworld")] #filter with one value in multiple columns`
  - `df.loc[df.a.isin(valuelist)] #filter with a few values in a list`
- [Assign value to specific column(s) by matching value](notebooks/pandas/df_assign_col_values.ipynb)
- Get a subset of dataframe by rows - `df.iloc[<from_rows>:<to_rows>, :]`
- [Count items and filter by counter values](notebooks/pandas/filter&valuecount.ipynb)
- [Retrieve columns name which match specific str](notebooks/pandas/filterbysubsetname.ipynb)


### Excel In/Out

- Read in excel with specific sheet name: `pd.read_excel(<url>, sheet_name = "Sheet1", engine = "openpyxl")`
  - Note: Install engine by `pip install openpyxl`
- [Read number of sheets in excel](notebooks/pandas/count_excel_sheets.ipynb)
- Save excel: `df.to_excel('file_name', index = False) `
- [Write to multiple sheets](notebooks/pandas/write_to_multiple_sheets_excel.ipynb)

### CSV In/Out

- Read csv with other delimiter `pd.read_csv(<path-to-file>, delimiter = '\x01')`
- Read csv with bad lines `pd.read_csv(<path-to-file>, on_bad_lines='skip')`
  - Note: `pd.read_csv(<path>, error_bad_lines = False)` deprecated
- Read csv with encoding `pd.read_csv('file name', encoding = 'utf-8')`
- Save to csv `df.to_csv('file name', index = False)`
  - Note: Put `index = False` is important to prevent an extra column of index being saved.
- Save to csv with encoding `df.to_csv('file name', encoding = 'utf-8')`


### [Parquet In/Out](notebooks/pandas/readwriteparquet.ipynb)

- Read in parquet: `pd.read_parquet(...)`
- Write to parquet: `pd.to_parquet(...)`

### Pickle In/Out

**Note: Pickle have security risk and slow in serialization (even to csv and json). Dont use**

- Read in pickle to dataframe: `df = pd.read_pickle(<file_name>) # ends with .pkl`
- Save to pickle: `df.to_pickle(<file_name>)`

## Numpy

- [Numpy basic](notebooks/numpy/npbasic.ipynb)
- [Numpy array to list]: ```nparray.tolist()```
- Numpy NaN (Not A Number): Constant to act as a placeholder for any missing numerical values in the array: `np.NaN / np.nan / np.NAN`
- [Numpy <> Binary File(.npy)](notebooks/numpy/np2binary.ipynb)
- [Numpy <> Bytes](notebooks/numpy/np2bytes.ipynb)


## Pytorch

- Given torch.tensor `buffer = tensor(4)`, get the value by - `id = buffer.item()`
- Given torch.tensor, get the argmax of each row - `torch.argmax(buffer, dim=<(int)dimension_to_reduce>)`
- Tensor to cuda - `inputs = inputs.to("cuda")`
- Check if cuda is available - `import torch; torch.cuda.is_available()`

### Torch Tensor
- Numpy array to torch tensor - `torch.from_numpy(np_array)`
- Tensor shape - `tensor.shape`
- Tensor data types - `tensor.dtype`
- Device tensor is stored on - `tensor.device`

## Huggingface

- Send model to cuda - `model.to('cuda:0')` or `model.cuda()`
- [Overview of DatasetDict](notebooks/huggingface/datasetdict_intro.ipynb)
- [DatasetDict from Pandas Dataframe](https://stackoverflow.com/questions/71618974/convert-pandas-dataframe-to-datasetdict)

## Audio

- [Audio of .wav -> .flac](notebooks/audio/wav2flac.ipynb)
- [Get sampling rate of an audio file](notebooks/audio/getsamplingrate.ipynb)
- [Audio file <> Numpy Array](notebooks/audio/audiofile2array.ipynb)

## Input

- [Get system input](notebooks/input/sysinput.py)

## Formatting

- datetime: [datetime.ipynb](notebooks/formatting/datetime.ipynb)
- Format floating value to n decimal: ```"%.2f" % floating_var```

## Data Structure

### List

- List of str to int: `list(map(int, arr))`
- List with range of values: `list(range(...))`
- Split str to list of str: `arr.split(" ")`
- Sort an array in place: `arr.sort()` / Return a sorted array: `sorted(arr)`
- Get index of a value: `arr.index(value)`
- Add one more value to existing list: `arr.append(value)`
- Extend list with values in another list: `arr.extend(arr2)`
- Check for empty list: `arr = []; if not arr: #empty list`
- Check all items in a list(subset) if exist in another list, returns boolean: `set(b).issubset(v)`
- Build list of same values: `['100'] * 20 # 20 items of the value '100'`
- Change values of list with **List Comprehension**: `[func(a) for a in sample_list]`
- Iteration of list with index: `for index, value in enumerate(inlist):`
- Iteration over two lists: `[<operation> for item1, item2 in zip(list1, list2)]```
- [Count occurence of items in list](notebooks/list/countoccurence.ipynb)

### Dictionary

- [Define dict with str keys](notebooks/dictionary/definedict.ipynb)
- Add new key value pair: `dict.update({"key2":"value2"})`
- Get keys as list: `list(lut.keys())`
- Get values as list: `list(lut.values())`
- Create dict from list: `{i: 0 for i in arr}`
- Find if key exists in existing dict: `if k in lut`
- [Iteration to dict to get keys and values](notebooks/dictionary/dict_iteration.ipynb)
- Save/load dictionary to/from a file: [saveloaddict.ipynb](notebooks/dictionary/saveloaddict.ipynb)
- Revert or inverse a dictionary mapping: `inv_map = {v: k for k, v in my_map.items()}`

### Python Iterables (List, Set,...)

- To identify if any items in the iterables has True/1 values: `any(sample_list) #returns single value True/False`

## Maths

- [Define Nan, Infinite](notebooks/math/define_nan_infinite.ipynb)
- Sum up an array: `sum(arr)`
- Round up a number to a certain decimal point: `round(value, 1)`
- [Calculate percentile](notebooks/math/percentile.ipynb)
- Randomly choosing an item out from a list: `import random; random.choice([123, 456, 378])`
- Power of a number: `pow(base_number, exponent_number`
- Square root of a number: `sqrt(number)`

### Random
- Generate random integer within (min, max): `from random import randint; randint(0, 100) #within 0 and 100`
- Generte random floating value: `from random import random; random()`

## File System

- The character used by the operating system to separate pathname components: `os.sep`
- [Iterate through a path to get files/folders of all the subpaths](notebooks/filesystem/filewalk.ipynb)
- Check if path is a folder: `os.path.isdir(<path>)`
- Create folder: `os.mkdir(<path>`
- Create folders recursively: `os.makedirs(<path>)`
- Expand home directory: `os.path.expanduser('~')`
- Get current running script path: `os.getcwd()`
- Get the list of all files and directories in the specified directory (does not expand to items in the child folder: `os.listdir(<path>)`
- Get current file path (getcwd will point to the running script(main) path, this will get individually py path): `os.path.dirname(os.path.abspath(__file__))`
- Append certain path: `sys.path.append(<path>)`
- Check if path exist: `os.path.exists(<path>)`
- Remove a file: `os.remove()`
- Get size of current file in byte: `os.path.getsize(<path>)` or `from pathlib import Path; Path(<path>).stat().st_size`
- Removes an empty directory: `os.rmdir()`
- Deletes a directory and all its contents: `shutil.rmtree()`
- [Copy a file to another path](notebooks/filesystem/copyfile.ipynb)
- [Unzip file](notebooks/filesystem/uncompresszip.ipynb)
- Check operating system: `import platform; platform.system()`

## String

- Check if string is empty, len = 0: `if not strvar:`
- Check if string contains digit: `any(chr.isdigit() for chr in str1) #return True if there's digit`
- Check file extension: [string/check_file_extension.ipynb](notebooks/string/check_file_extension.ipynb)
- Capitalize a string: `strvar.capitalize()`
- Uppercase a string: `strvar.upper()`
- Lowercase a string: `strvar.lower()`
- Remove white spaces in the beginning and end: `strvar.strip()`
- Swap existing upper and lower case: `strvar.swapcase()`
- Capitalize every first letter of a word: `strvar.title()`
- Split a string based on character: `strvar.split(<char>)`
  - If split with every character, do this instead: `[i for i in "ABCDE"]`
  - Split on white space `strvar.split()`
- Check if string starts with a substring: `strvar.startswith(<substring>)`
- Check if string ends with a substring: `strvar.endswith(<substring>)`
- Check if string have substring/specific character. Returns -1 if not found. : `strvar.find(<substring>)`
- String get substring with index: `str[startindex:endindex]`
- Replace string/character with intended string/character: `strout = strin.replace(" ", "_")`
- [Replace multiple string/characters with intended string/character](notebooks/string/replace_multiple_character.ipynb)
- [Generate random string](https://pynative.com/python-generate-random-string/)

## Class

- [Effective way to view object address and object](notebooks/class/class_object_view.ipynb)
- [Reserved methods in class](notebooks/class/reservedMethod.py)
- [The magic variable \*args and \*\*kwargs](notebooks/class/kwargsimp.py)
- [Abstract class with ABCMeta and @abstractmethod](notebooks/class/abstractmethod.py)
- [getter: @property, setter: @{variable}.setter, deleter: @{variable}.deleter](notebooks/class/property.ipynb)
- [Deep Copy, Shallow Copy](notebooks/class/deepcopy_shallowcopy.ipynb)
  - Copy list by value: `list_cp = list_ori[:]` (Note: `list_cp = list_ori` copy by reference)

## Processing iterables with a functional style

- [Produce a new iterable with map()](notebooks/functional/mapimp.ipynb)
- [Generate a new iterable with Boolean-return function with filter()](notebooks/functional/filterimp.ipynb)
- [Produce a single cumulative value from iterable with reduce()](notebooks/functional/reduceimp.ipynb)
- [Condition checking with any(<iterable>)](notebooks/functions/anyimp.ipynb)

_Note: Functional style can be replaced with **list comprehension** or **generator expressions**_

## ConfigParser

- Read from config file: [configparser/testconfig.ipynb](notebooks/configparser/testconfig.ipynb)

## URL

- [Download URL to local file and checksum](notebooks/url/downloadurl.ipynb)

## Performance

- [Dataframe - column-major, Numpy - row-major](notebooks/performance/df_numpy_major.ipynb)

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

### Logging

- [Logging with module _icecream_](notebooks/logging/icecream)

## Design Patterns

- [Abstract Factory](notebooks/designpatterns/abstractfactory.py)
- [Monkey Patching](notebooks/designpatterns/monkeypatching.py)
- [Singleton](notebooks/designpatterns/singleton.py)

### [Built-in Decorators](notebooks/decorator/built-in-decorators.md)
- [Class Method](notebooks/decorator/classmethod.py)
- [Static Method](notebooks/decorator/staticmethod.py)
- [dataclass]
  - [dataclass hello world](notebooks/decorator/dataclasshelloworld.py)

## Others

- [Type Checking with module _typing_](notebooks/module/typing_imp.ipynb)

## Medium Posts

- [Ctrl + c, Ctrl + v — Replicating Data Science Conda Environment](https://codenamewei.medium.com/ctrl-c-ctrl-v-replicating-data-science-conda-environment-c190ad0d93fd)
  - [Conda Commands Cheatsheet](miniconda-guidelines.md)
- [Displaying visuals with Markdown](https://medium.com/geekculture/displaying-visuals-with-markdown-c39f2495e146)
  - [Examples of displaying image in readme.md](https://github.com/codenamewei/pydata-science-playground/blob/main/notebooks/markdown/readme.md)
  - [Examples of displaying image in Jupyter](https://github.com/codenamewei/pydata-science-playground/blob/main/notebooks/markdown/markdown_guidelines.ipynb)
