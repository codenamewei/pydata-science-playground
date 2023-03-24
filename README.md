# Snippets of Code for Data Science Operations in Python

<div align="center">
  <img alt="datascienceplaygronud" src="metadata/pydatascienceplayground.png"><br>
</div>

<p>
  <p align="left">
<img alt="project status: active" src="https://img.shields.io/badge/Project%20Status-%F0%9F%94%A5Active-brightgreen">

</p>

## Environment Setup

**Create environment (Only for the first time)**

```
git clone https://github.com/codenamewei/pydata-science-playground.git
cd <path-to>/pydata-science-playground
conda env create -f config.yml
```

**Activate environment**

`conda activate pyplayground`

## Package Installation

**Install package with pip**  
`pip install <package-name>`. Example:`pip install numpy`

- For more pip commands, check out [pip guidelines document](pip-guidelines.md)

**Install package with conda**

`conda install <package>`. Example: `conda install numpy`

- For more conda commands, check out [conda guidelines document](conda-guidelines.md)

## Basic

### Comment
  
- Single Line Comment: `//sample text`
- Multi Lines Comment:
  ```
   """
   Hello World!
   Nice to meet all of you cookie monsters!
   """
  ```

### Boolean Operator

- [X and Y](notebooks/boolean_operator/boolean_options.ipynb)
- [X or Y](notebooks/boolean_operator/boolean_options.ipynb)
- [if not X](notebooks/boolean_operator/boolean_options.ipynb)
- [custom object boolean](notebooks/boolean_operator/boolean_for_object.ipynb)

### [Maths](notebooks/math)

- [Define Nan, Infinite](notebooks/math/define_nan_infinite.ipynb)
- Sum up an array: `sum(arr)`
- Round up a number to a certain decimal point: `round(value, 1)`
- [Calculate percentile](notebooks/math/percentile.ipynb)
- Power of a number: `pow(base_number, exponent_number`
- Square root of a number: `sqrt(number)`
- Logarithm / Log
  - Log to the base of 2:
    - Numpy: `import numpy as np; np.log2(10)`
    - Math: `import math; math.log2(10)`
    - [Plotting of log to the to the base of 2](notebooks/math/logn_plotting.ipynb)


### Data Types
    
#### Floating Value (float, double)

- Format floating value to n decimal: `"%.2f" % floating_var`

#### Bytes

**Notes:**

```
Difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified (immutable), 
and bytearray() returns an object that can be modified (mutable).
```

- [Numpy <> Bytes, Bytes <> Numpy](notebooks/numpy/np2bytes.ipynb)
- [Bytes -> String](notebooks/string/bytes2string.ipynb): `bytesobj.decode("utf-8")`
- String -> Bytes: `strobj.encode("utf-8")`
- [Bytes -> Multimedia file (video/audio))](src/bytesops/readme.md)
- [Check bytes encoding](notebooks/bytearrayops/checkbytesarrayencoding.ipynb)
- To Bytes: `bytes(<value>)`
- Get size of bytes object: `import sys;sys.getsizeof(bytesobject)`
- [Split bytes to chunks](notebooks/bytesops/bytestochunk.ipynb)

#### ByteArray
  
**Notes:**

```
Difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified (immutable), 
and bytearray() returns an object that can be modified (mutable).
```

- [Integer to Bytearray](notebooks/bytearrayops/bytearraybasic.ipynb)
- [Native Array to Bytearray](notebooks/bytearrayops/bytearraybasic.ipynb)
- [Numpy Array to Bytearray](notebooks/bytearrayops/bytearraybasic.ipynb)
- [Image as Bytearray](notebooks/cv/image_as bytearray.ipynb)
- [Check bytes array encoding](notebooks/bytearrayops/checkbytesarrayencoding.ipynb)
- To ByteArray: `bytearray(<value>)`
  
#### Numpy
  
- [Numpy basic](notebooks/numpy/npbasic.ipynb)
- Get numpy shape: `nparray.shape`
- Numpy array to list: `nparray.tolist()`
- Change datatype: `nparray = nparray.astype(<dtype>)` Example: `nparray = nparray.astype("uint8")`
- Numpy NaN (Not A Number): Constant to act as a placeholder for any missing numerical values in the array: `np.NaN / np.nan / np.NAN`
- Numpy multiply by a value: `nparray = nparray * 255`
- [Numpy array to image](notebooks/pytorch/torchtensor2image.ipynb)
- [Numpy <> Binary File(.npy)](notebooks/numpy/np2binary.ipynb)
- [Use of `numpy.where`](notebooks/cv/blur_region.ipynb)
  

### Data Structure

#### [List](notebooks/list)
  
- List of str to int: `list(map(int, arr))`
- List with range of values: `list(range(...))`
- Split str to list of str: `arr.split(" ")`
- Check for empty list: `if not mylist:`
- Find if a value in a list: `if value in mylist:` / `if value not in mylist:`
- Sort an array in place: `arr.sort()` / Return a sorted array: `sorted(arr)`
- Get index of a value: `arr.index(value)`
- Add one more value to existing list: `arr.append(value)`
- Extend list with values in another list: `arr.extend(arr2)`
- Remove an item from the list: `arr.remove(item)`
- Check for empty list: `arr = []; if not arr: #empty list`
- Check all items in a list(subset) if exist in another list, returns boolean: `set(b).issubset(v)`
- Build list of same values: `['100'] * 20 # 20 items of the value '100'`
- Change values of list with **List Comprehension**: `[func(a) for a in sample_list]`
- Iteration of list with index: `for index, value in enumerate(inlist):`
- Iteration over two lists: `[<operation> for item1, item2 in zip(list1, list2)]```
- [Count occurence of items in list](notebooks/list/countoccurence.ipynb)
- Get maximum value in a list of numbers (even strings): `max(samplelist)`
  
#### [Dictionary](notebooks/dictionary)
  
- [Define dict with str keys](notebooks/dictionary/definedict.ipynb)
- Add new key value pair: `dict.update({"key2":"value2"})`
- [Remove key<> value pair by referring to specific key](notebooks/dictionary/remove_key.ipynb)
- Get keys as list: `list(lut.keys())`
- Get values as list: `list(lut.values())`
- Create dict from list: `{i: 0 for i in arr}`
- [Handling missing items in dict](notebooks/dictionary/nativedict_handlemissingkey.ipynb)
- [Iteration to dict to get keys and values](notebooks/dictionary/dict_iteration.ipynb)
- [Save/load dictionary to/from a file](notebooks/dictionary/saveloaddict.ipynb)
- Revert or inverse a dictionary mapping: `inv_map = {v: k for k, v in my_map.items()}`
- [Copy by value](notebooks/dictionary/dict_copybyvalue.ipynb): `sampledict.copy()`
  
### Python Iterables (List, Set,...)

- To identify if any items in the iterables has True/1 values: `any(sample_list) #returns single value True/False`
- [Zip multiple iterables](notebooks/zipops/zipops.ipynb)

### [Pandas](https://pandas.pydata.org/docs/reference/)

<details>
 
#### Panda Infos

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

#### Panda Operations

- Check if dataframe is empty: `df.empty #return boolean`
- [Get dataframe from list](notebooks/pandas/list2df.ipynb)
- Build dataframe with columns name
  ```
  column_list = ["a", "b"]
  df = pd.DataFrame(columns = column_list)
  ```
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
- [Append string to all rows of a column](notebooks/pandas/append_value_to_row.ipynb)
- Reset index without creating new (index) column: `df.reset_index(drop=True)`
- Assign df by copy instead of reference - [`df.copy()`](notebooks/pandas/copybyvalue.ipynb)
- Shuffle rows of df: `df = df.sample(frac=1).reset_index(drop=True)`
- [Pandas with multiple index](notebooks/pandas/pd_multiple_index.ipynb)

#### Panda Type

- [Change column type](notebooks/pandas/change_column_type.ipynb)
- [Rename column name if exist](notebooks/pandas/rename_column.ipynb)
- [Compare column type](notebooks/pandas/comparecoltype.ipynb)

#### Panda Series

- [Series to value](notebooks/pandas/series_to_values.ipynb)
- Series/Dataframe to numpy array: `input.to_numpy()`
- Series iteration: `for index, item in seriesf.items():`
- Series to dict: `seriesf.to_dict()`

#### Panda Assign values

- [Create new column and assign value according to another column](notebooks/pandas/assign_column.ipynb)
- [Assign values by lambda and df.assign](notebooks/pandas/dfassign.ipynb)
- [Dataframe append rows](notebooks/pandas/df_append_rows.ipynb)

#### Panda Remove/drop values

- [Drop duplicates for df / subset, keep one copy and remove all](notebooks/pandas/drop_duplicate.ipynb)
- [Remove/drop rows where specific column matched value](notebooks/pandas/remove_with_matching_value.ipynb)
- [Remove specific columns with column name](notebooks/pandas/remove_column.ipynb)
- [Drop rows by index](notebooks/pandas/drop_row_by_index.ipynb)
- Drop rows/columns with np.NaN: `df3 = df3.dropna(axis = 1) #row`

#### Panda SQL-like functions

- pivot table - tbd
  - Drawback: Not able to do filtering selection
- [Merge two dataframes based on certain column values](notebooks/pandas/pdmerge.ipynb)

#### Panda Filtering

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

#### Panda Excel In/Out

- Read in excel with specific sheet name: `pd.read_excel(<url>, sheet_name = "Sheet1", engine = "openpyxl")`
  - Note: Install engine by `pip install openpyxl`
- [Read number of sheets in excel](notebooks/pandas/count_excel_sheets.ipynb)
- Save excel: `df.to_excel('file_name', index = False) `
- [Write to multiple sheets](notebooks/pandas/write_to_multiple_sheets_excel.ipynb)

#### Panda CSV In/Out

- Read csv with other delimiter `pd.read_csv(<path-to-file>, delimiter = '\x01')`
- Read csv with bad lines `pd.read_csv(<path-to-file>, on_bad_lines='skip')`
  - Note: `pd.read_csv(<path>, error_bad_lines = False)` deprecated
- Read csv with encoding `pd.read_csv('file name', encoding = 'utf-8')`
- Save to csv `df.to_csv('file name', index = False)`
  - Note: Put `index = False` is important to prevent an extra column of index being saved.
- Save to csv with encoding `df.to_csv('file name', encoding = 'utf-8')`

#### Panda JSON In/Out

- [Read in json](notebooks/json/readfromjson.ipynb)
- [Write to json](notebooks/json/write2json.ipynb)

#### Panda [Parquet In/Out](notebooks/pandas/readwriteparquet.ipynb)

- Read in parquet: `pd.read_parquet(...)`
- Write to parquet: `pd.to_parquet(...)`

#### Panda Pickle In/Out

**Note: Pickle have security risk and slow in serialization (even to csv and json). Dont use**

- Read in pickle to dataframe: `df = pd.read_pickle(<file_name>) # ends with .pkl`
- Save to pickle: `df.to_pickle(<file_name>)`

#### Panda Dataframe Others

- [Random dataframe and database table generator](https://github.com/tirthajyoti/pydbgen)

</details>

### Random

- Generate random integer within (min, max): `from random import randint; randint(0, 100) #within 0 and 100`
- Generate random floating value: `from random import random; random()`
- Randomly choosing an item out from a list: `import random; random.choice([123, 456, 378])`
- Generate list with random number: `import random; random.sample(range(10, 30), 5)`
  - Example shown where 5 random numbers are generated in between 10 to 30

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Intermediate

## Advanced

## [Audio](notebooks/audio)

- [Audio of .wav -> .flac](notebooks/audio/wav2flac.ipynb)
- [Get sampling rate of an audio file](notebooks/audio/getsamplingrate.ipynb)
- [Audio file <> Numpy Array](notebooks/audio/audiofile2array.ipynb)








## [File System](notebooks/filesystem)

- The character used by the operating system to separate pathname components: `os.sep`
- [Iterate through a path to get files/folders of all the subpaths](notebooks/filesystem/filewalk.ipynb)
- Write file: `f.write(str)`
- print without new line: `print(..., end="")
- Get environment path (second param is optional)
  - `import os; os.getenv(<PATH_NAME> : str, <alternative-return-value>: str)
- [Flush out print](notebooks/filesystem/stdoutflush.ipynb)
- Check if path is a folder: `os.path.isdir(<path>)`
- [Get file size](notebooks/filesystem/getfilesize.ipynb)
  - `from pathlib import Path; outsize : int = Path(inputfilepath).stat().st_size`
  - `import os; outsize : int = os.path.getsize(inputfilepath)`
- Create folder: `os.mkdir(<path>`
- Create folders recursively: `os.makedirs(<path>)`
- Get folder path out of given path with filename: `os.path.dirname(<path-to-file>)`
- Expand home directory: `os.path.expanduser('~')`
- Get current running script path: `os.getcwd()`
- Get the list of all files and directories in the specified directory (does not expand to items in the child folder: `os.listdir(<path>)`
- Get current file path (getcwd will point to the running script(main) path, this will get individually py path): `os.path.dirname(os.path.abspath(__file__))`
- Get filename from path: `os.path.basename(configfilepath)`
- Split extension from rest of path(Including .): `filename, ext = os.path.splitext(path)`
- Append certain path: `sys.path.append(<path>)`
- Check if path exist: `os.path.exists(<path>)`
- Remove a file: `os.remove()`
- Get size of current file in byte: `os.path.getsize(<path>)` or `from pathlib import Path; Path(<path>).stat().st_size`
- Removes an empty directory: `os.rmdir()`
- Deletes a directory and all its contents: `shutil.rmtree()`
- [Copy a file to another path](notebooks/filesystem/copyfile.ipynb)
- [Unzip file](notebooks/filesystem/uncompresszip.ipynb)
- [Readfile](notebooks/filesystem/readfile.ipynb)
  <details>

  ```
  open(<path-to-file>, mode)
  ```

  - `r`: Open for text file for reading text
  - `w`: Open a text file for writing text
  - `a`: Open a text file for appending text
  - [`b`: Open to read/write as bytes](notebooks/cv/image_as_byte.ipynb)
    Read file has 3 functions

  - `read()` or `read(size)`: read all / size as one string.
  - `readline()`: read **a single line** from a text file and return the line as a string.
  - `readlines()`: read all the lines of the text file into a list of strings.
  - `write(<param> : str)`: write in param. Need to explicitly add `\n` to split line.
  - `.close()`: close file iterator
  </details>

## System

- [Get system input](notebooks/system/sysinput.py)
- Check operating system: `import platform; platform.system()`
- [Check if port is open/close](notebooks/system/check_port_open.ipynb)

## Unique Identifer (UUID)

- [Generate unique identifer UUID](notebooks/uuid/uuidops.ipynb)
- [Validate if a string is UUID](notebooks/uuid/uuidops.ipynb)
- [Compare if both UUID are the same](notebooks/uuid/uuidops.ipynb)
- UUID to string: `str(uuidparam)`

## Datetime
- datetime: [datetime.ipynb](notebooks/formatting/datetime.ipynb)
- [find differences of two datetime: use divmod](https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python)

## String

- Generate string with parameter
  - [Using template literal](notebooks/string/paramwithstring.ipynb): `print(f'Completed part {id}')
  - [Generate string with templates](notebooks/string/stringtemplate.ipynb)
  - String formatting method: `print('Completed part {part_id}'.format(part_id))`
  - create string in the raw format `varname="world"; print(f"Hello {varname!r}")
- Check if string is empty, len = 0: `if not strvar:`
- Check if string contains digit: `any(chr.isdigit() for chr in str1) #return True if there's digit`
- Check file extension: [notebooks/string/check_file_extension.ipynb](notebooks/string/check_file_extension.ipynb)
- Capitalize a string: `strvar.capitalize()`
- Uppercase a string: `strvar.upper()`
- Lowercase a string: `strvar.lower()`
- Get substring from a string: `strvar[<begin-index>:<end-index>]` / `strvar[<begin-index>:]` / `strvar[:<end-index>]`
- Remove white spaces in the beginning and end: `strvar.strip()`
- Swap existing upper and lower case: `strvar.swapcase()`
- Capitalize every first letter of a word: `strvar.title()`
- Splitting string:
  - Split a string based on separator: `strvar.split(separator)` Example: `strvar.split("x")`
  - Split on white space `strvar.split()`
  - If split with every character, do this instead: `[*"ABCDE"]` Result: `["A", "B", "C", "D", "E"]`
- Check if string starts with a substring: `strvar.startswith(<substring>)`
- Check if string ends with a substring: `strvar.endswith(<substring>)`
- Check if string have substring/specific character. Returns -1 if not found. : `strvar.find(<substring>)`
- String get substring with index: `str[startindex:endindex]`
- Replace string/character with intended string/character: `strout = strin.replace(" ", "_")`
- [Replace multiple string/characters with intended string/character](notebooks/string/replace_multiple_character.ipynb)
- [Generate random string](https://pynative.com/python-generate-random-string/)
- List to string: ` <separators>.join(list) example: ', '.join(listbuffer)`

## [Regular Expression (Regex)](notebooks/regex)

- [Find matching word/character 1](notebooks/regex/charactermatch.ipynb)
  - Introduction of functions in _re_ library
  - Square brackets for upper and lower case `[Ww]oodchuck`
- [Find matching word/character 2](notebooks/regex/charactermatch2.ipynb)
  - Optional character with `?`
  - Optional 0 or more character with `*`
  - Optional 1 or more character with `+`
  - Any character with `.`
- [Find matching word/character 3](notebooks/regex/charactermatch3.ipynb)
  - Whitespace character find with `\s`
  - Non-whitespace character find with `\S`
- [Find matching word/character 4](notebooks/regex/charactermatch4.ipynb)
  - Caret before square bracket:`^[]` to indicate beginning
  - Dollar sign after square bracket:`[]$` to indicate ending
- [Negation](notebooks/regex/negation.ipynb)
- [Disjunction](notebooks/regex/disjunction.ipynb)
  - To match a series of patterns with parenthesis.
- [Extract hashtags](notebooks/regex/filterhashtag.ipynb)
- [Extract numbers from string](notebooks/regex/extractnumbersfromstr.ipynb)

## Collections Module

- [NamedTuple](notebooks/collections_imp/namedtupleimp.ipynb)

## Class

- [Effective way to view object address and object](notebooks/class/class_object_view.ipynb)
- [Reserved methods in class](notebooks/class/reservedMethod.py)
- [The magic variable \*args and \*\*kwargs](notebooks/class/kwargsimp.py)
- [Check if object is of specified type](notebooks/class/isinstanceimp.ipynb): `isinstance(obj, MyClass)` / `isinstance(obj, (type1, type2) : tuple)`
- [Deep Copy, Shallow Copy](notebooks/class/deepcopy_shallowcopy.ipynb)
  - Copy list by value: `list_cp = list_ori[:]` (Note: `list_cp = list_ori` copy by reference)
- Define dataclass
  - [dataclass 1](notebooks/class/dataclass/dataclass_helloworld_1.ipynb)
  - [dataclass 2](notebooks/class/dataclass/dataclass_helloworld_2.ipynb)
    - Magic methods `__repr__` and `__dict__` are created when define class with dataclass
- [Implement Enum in Python](notebooks/class/enumimpl.ipynb)
- [Serialize class object](notebooks/class/classobj.ipynb)

### Magic Method

- [`__dict__` return all attributes of an object(only those defined in __init__): `obj.__dict__`](notebooks/class/values_in_dict.ipynb)
- `__str__` return string representation of the obj: `def __str__(self):`
- `__eq__` compare the instances of the class: `def __eq__(self, other):`
  - [Define **eq** function in class 1](notebooks/class/eq_function.ipynb)
  - [Define **eq** function in class 2](notebooks/class/dataclass_helloworld_1.ipynb)
- [`__repr__`: represent a class's objects as a string. Call object with `repr(obj)`](notebooks/class/magic_repr.ipynb)

### Inheritance

- [from abs import ABC](notebooks/error_handling/error_types/notimplementederror.ipynb)
- [from abs import ABCMeta](notebooks/decorator/abstractmethod.py)
- [Difference between importance ABC or ABCMeta](https://stackoverflow.com/questions/33335005/is-there-any-difference-between-using-abc-vs-abcmeta)
  - TLDR: ABC is a wrapper of ABCMeta, both serves the purpose where former easy to write.

## Passing variables in from command line

- [Unnamed arguments](notebooks/command_line/sysarg.py)
- Named arguments: TBD
- [Filename as argument](notebooks/command_line/fileargparse.py)

## Processing iterables with a functional style

- [Produce a new iterable with map()](notebooks/functional/mapimp.ipynb)
- [Generate a new iterable with Boolean-return function with filter()](notebooks/functional/filterimp.ipynb)
- [Produce a single cumulative value from iterable with reduce()](notebooks/functional/reduceimp.ipynb)
- [Condition checking with any(<iterable>)](notebooks/functional/anyimp.ipynb)
- [Multiple function declaration with singledispatch)](notebooks/functional/singledispatchimp.ipynb)

_Note: Functional style can be replaced with **list comprehension** or **generator expressions**_

## ConfigParser

- [Read from config file:](notebooks/configparser/testconfig.ipynb)


## XML Parser
- [Read from xml file:](notebooks/xmlparser)

## URL

- [Download URL to local file and checksum](notebooks/url/downloadurl.ipynb)

## Performance

- [Dataframe - column-major, Numpy - row-major](notebooks/performance/df_numpy_major.ipynb)

### Multiprocessing

- [Create workers according to number of cores](src/multiprocess_ops/readme.md)

## Time

- [Measure time prior and after](notebooks/performance/count_time.ipynb)
- Add delay to execution of the program by pausing: `import time;time.sleep(seconds)`
  - Note: stops the execution of current thread only

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
- Log with variables: `logging.error(f"Keys {a} is missing")`
- [Log exception](notebooks/error_handling/suppress_error/urlcaller_logger.py)

### Logging

- [Logging with module _icecream_](notebooks/logging/icecream)

## Design Patterns

- [Abstract Factory](notebooks/designpatterns/abstractfactory.py)
- [Monkey Patching](notebooks/designpatterns/monkeypatching.py)
- [Singleton](notebooks/designpatterns/singleton.py)

### [Built-in Decorators](notebooks/decorator/built-in-decorators.md)

- [Class Method](notebooks/decorator/classmethod.py)
- [Static Method](notebooks/decorator/staticmethod.py)
- dataclass
  - [dataclass hello world](notebooks/decorator/dataclass_helloworld.ipynb)
- [Abstract class with ABCMeta and @abstractmethod](notebooks/decorator/abstractmethod.ipynb)
- [Property Setting](notebooks/decorator/property.ipynb)
- [@property to prevent setting value](notebooks/decorator/property_notsetvalue.ipynb)
  1. Native Verbose Method
  2. Using built-in property function
  3. Using decorator
  - getter: @property
  - setter: @{variable}.setter
  - deleter: @{variable}.deleter

## Type Checking, Data Validation

- [Module _typing_: Type hint & annotations](notebooks/type_checking/typingimp.ipynb)
  - [Dict](notebooks/type_checking/anyimp.ipynb)
  - List
  - Tuple
  - Set
  - [Any](notebooks/type_checking/anyimp.ipynb)
  - [Union](notebooks/type_checking/unionimp.ipynb)
- Module _pydantic_: Data parsing and validation library: TBA

## Error Handling

- [Native Catching Exception](notebooks/error_handling/catcherror.ipynb)
- [Traceback](notebooks/error_handling/traceback)
- [Suppress and log error](notebooks/error_handling/suppress_error)

### [Types of Built-In Exceptions](https://docs.python.org/3/library/exceptions.html)

- [ValueError: argument of the correct data type but an inappropriate value](notebooks/error_handling/error_types/valueerror.ipynb)
- [TypeError: the data type of an object is incorrect](notebooks/error_handling/error_types/typeerror.ipynb)
- [IndexError: Raised when a sequence subscript is out of range](notebooks/error_handling/error_types/indexerror.ipynb)
- [KeyError: When key cannot be found](notebooks/error_handling/keyerror.ipynb)
- [ZeroDivisionError: when a number is divided by zero](notebooks/error_handling/error_types/zerodivisionerror.ipynb)
- [OSError: error from an os-specific function](notebooks/error_handling/error_types/oserror.ipynb)
- [FileNotFoundError: when a file or directory is requested but doesn’t exist](notebooks/error_handling/error_types/filenotfounderror.ipynb)
- [NotImplementedError: commonly raised when an abstract method is not implemented in a derived class](notebooks/error_handling/error_types/notimplementederror.ipynb)
- [NameError: reference to some name (variable, function, class) that hasn’t been defined](notebooks/error_handling/error_types/nameerror.ipynb)
- [AttributeError: reference to certain attribute in a class which does not exist](notebooks/error_handling/error_types/attributeerror.ipynb)
- [ImportError: Trouble loading a module](notebooks/error_handling/metadata/importerror.jpg)
  - Submodule
    - ModuleNotFoundError: the module trying to import can’t be found or try to import something from a module that doesn’t exist in the module

### Others

- [Kill after x amount of time if process not complete](src/error_handling/timeout)

## Networking
  
- Get IP from domain name: `import socket;socker.gethostbyname("www.google.com");`
  
## Concurrency

### Built-in Concurrency Library: Asyncio

- [Simple example with asyncio](notebooks/concurrency/asyncio/asyncio_wait.py)

## Hashing 
 
- [Password hashing with library bcrypt - saltround)(notebooks/hashing/bcrypt_password_hashing.ipynb)

## Web

- [Webhook](src/web/webhook)

## Database

- [Connect to db with sqlalchemy](notebooks/sqlalchemyops/readme.md)

### [PostgreSQL](notebooks/postgresql-python/readme.md)

- [Postgres connect to AWS RDS](notebooks/postgresql-python/notebooks/aws-rds)
- [Local Node](notebooks/postgresql-python/notebooks/local)
- [Save and load image between REST and Postgres](notebooks/postgresql-python/notebooks/restimage2postgres)
- [Save and load video between REST and Postgres](notebooks/postgresql-python/notebooks/restvideo2postgres)

## REST

### FastAPI

- [Form Data](src/rest/fastapi/formdataexample)
- [Send image via UploadFile](notebooks/postgresql-python/notebooks/image2postgres/server.py)
- [Client upload file to FastAPI Uploadfile and get response](notebooks/rest/fastapi/clientsendfile.ipynb)
- [Return content from url and write image](notebooks/postgresql-python/notebooks/image2postgres/client.py)

### Requests

- [Get data from url](notebooks/rest/requests/download_from_url.ipynb)

## Cloud

### AWS

- [Postgres connect to AWS RDS](notebooks/postgresql-python/notebooks/aws-rds)

#### [S3: Scalable Storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorials.html)

- [List name of buckets](notebooks/cloud/aws/getbucketlist.ipynb)
- [List objects in a specific bucket](notebooks/cloud/aws/getobjectinbucketlist.ipynb)
- [Upload file with function upload_file or upload_fileobj](notebooks/cloud/aws/upload2bucket.ipynb)
  - [Upload video file](notebooks/cloud/aws/uploadvideo2bucket.ipynb)
  - [Upload video file with progress counter](notebooks/cloud/aws/uploadvideo2bucketwithprogress.ipynb)
- [Upload multipart](notebooks/cloud/aws/uploadmultipart.ipynb)
- [Upload multipart with multiple workers](src/cloud/aws/uploadmultipart_withworkers.py)
- [Get object from S3](notebooks/cloud/aws/getobject.ipynb)

**Note:**

- **What is a bucket in S3**
  <details>

  A bucket is a container for objects stored in Amazon S3 which can contains files and folders.
  You can store any number of objects in a bucket and can have up to 100 buckets in your account

  </details>

## Pytorch

- Check if cuda is available - `import torch; torch.cuda.is_available()`
- [Softmax](notebooks/pytorch/torch_softmax.ipynb)

### Torch Tensor

#### Torch Tensor Creation

- Create tensor of **zeros** with shape like another tensor: `torch.zeros_like(another_tensor)`
- Create tensor of **zeros** with shape (tuple): `torch.zeros(shape_in_tuple)`
- Create tensor of **ones** with shape like another tensor: `torch.ones_like(another_tensor)`
- Create tensor of **ones** with shape (tuple): `torch.ones(shape_in_tuple)`
- Create tensor of **random floating value** between 0-1 with shape like another tensor:  
  `torch.rand_like(another_tensor, dtype = torch.float)`
- Create tensor of **random floating value** between 0-1 with shape (tuple):  
  `torch.rand(shape_in_tuple)`

#### Torch Tensor Info Extraction

- Given torch.tensor `buffer = tensor(4)`, get the value by - `id = buffer.item()`
- Given torch.tensor, get the argmax of each row - `torch.argmax(buffer, dim=<(int)dimension_to_reduce>)`
- Tensor to cuda - `inputs = inputs.to("cuda")`
- Tensor shape - `tensor.shape`
- Tensor data types - `tensor.dtype`
- Device tensor is stored on - `tensor.device`
- Torch tensor(single value) to value: `tensorarray.item()`
- Retrieve subset of torch tensor by row index: `tensor[<row_number>, :]` / `tensor[<row_number_from>:<row_number_to>, :]`
- Retrieve subset of torch tensor by column index: `tensor[:, <column_number_from>:<column_number_to>]`

#### Torch Tensor Conversion

- List to torch tensor - `torch.tensor(listimp)`
- Numpy array to torch tensor - `torch.from_numpy(np_array)`
- [Image to torch tensor](notebooks/pytorch/torchtensor2image.ipynb)
- [Torch tensor to image](notebooks/pytorch/torchtensor2image.ipynb)

#### Torch Tensor Operation

- [Torch tensor value change by indexing and conditions](notebooks/pytorch/tensorvalue_manipulation.ipynb)
- [Concatenate tensor according to dimension (0 for adding rows, 1 for adding columns)](notebooks/pytorch/tensorvalue_manipulation_0.ipynb):  
  `torch.cat([<tensor_1>, <tensor_2>, ...], dim = <dimension_number>`

### Dataset Loader, Iterator

- `torch.utils.data.DataLoader`: stores the samples and their corresponding labels,
- `torch.utils.data.Dataset`: wraps an iterable around the Dataset to enable easy access to the samples

#### Torch Tensor In/Out

- [Save torch tensor to file](notebooks/pytorch/save_write_torch.ipynb): `torch.save(x : torch.tensor, tensorfile :str)`
- [Load torch tensor from file](notebooks/pytorch/save_write_torch.ipynb): `torch.load(tensorfile :str)`

### Dataset

- [Image Datasets](https://pytorch.org/vision/stable/datasets.html)

  - Fashion MNIST [Torch](https://github.com/pytorch/vision/blob/main/torchvision/datasets/mnist.py)
      <details>

    Fashion-MNIST is a dataset of Zalando’s article images consisting of 60,000 training examples and 10,000 test examples.
    Each example comprises a 28×28 grayscale image and an associated label from one of 10 classes.

      </details>

- [Text Datasets](https://pytorch.org/text/stable/datasets.html)
- [Audio Datasets](https://pytorch.org/audio/stable/datasets.html)

## Huggingface

- Send model to cuda - `model.to('cuda:0')` or `model.cuda()`
- [Overview of DatasetDict](notebooks/huggingface/datasetdict_intro.ipynb)
- [DatasetDict from Pandas Dataframe](https://stackoverflow.com/questions/71618974/convert-pandas-dataframe-to-datasetdict)

## OpenCV / Computer Vision

### Basic

- Get image shape: `img.shape`
- Create a color image: `image = np.zeros((h,w,3), np.uint8)`
- Read/Write image:
  - [As byte](notebooks/cv/image_as_byte.ipynb)
  - [As Bytearray](notebooks/cv/image_as_bytearray.ipynb)
  - [As base64](notebooks/cv/image_as_base64.ipynb)
- [Read image from url](notebooks/cv/read_image_from_url.ipynb)
- Pause to display image or wait for an input: `cv2.waitKey(0)`
- Save an image: `cv2.imwrite(pathtoimg : str, img : numpy.ndarray)`
- Show an image in window: `cv2.imshow(windowname : str, frame : np.array)`
- Show an image in Jupyter notebok
  ```
  from IPython.display import Image
  Image(filename=pathtoimg : str)
  ```
- Flip image: `frame = cv2.flip(frame, flipcode : int)`
  - Positive flip code for flip on y axis (left right flip)
  - 0 for flip on x axis (up down)
  - Negative for flipping around both axes

### Intermediate

### Filter

- [Blur](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga8c45db9afe636703801b0b2e440fce37) with averaging mask: `cv2.blur(img,(5,5))`
- GaussianBlur: `blur = cv2.GaussianBlur(img,(5,5),0)`
  - Note: Kernel size `(5, 5)` to be positive and odd. Read more [here](https://plantcv.readthedocs.io/en/v2.0/gaussian_blur/) on how kernel size influence the degree of blurring.
- [Blurring region of image](notebooks/cv/blur_region.ipynb)

### Video Stream

- Concat multiple video streams to show side by side: [2 video streams](src/cv/concat2windows.py) [3 video streams](src/cv/concat3windows.py)
- [Save stream to video output](src/cv/save2video.py)
- [Read in video stream from a file](src/cv/readvideostream.py)
- [Read in stream from camera](src/cv/save2video.py)
- [video arrays (in opencv) -> bytes -> np.array -> video arrays (in opencv)](src/cv/video2bytes2nparray.py)
- [Merge audio with video](src/cv/savevideowithaudio)
- [Check if video comes with audio](notebooks/cv/check_video_with_audio.ipynb)
- [Split audio from video](src/cv/splitaudiofromvideo.py)

#### Other

- [Overlay image](src/cv/replaceroi.py)
- Resizing frame: `outframe = cv2.resize(frame, (w, h))`
- [Set color to rectangle region](notebooks/cv/setrectangle.ipynb)
- Color to gray image: `gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`
- [Remove background](notebooks/cv/remove_bg.ipynb)
- [Add channel to image](https://stackoverflow.com/questions/32290096/python-opencv-add-alpha-channel-to-rgb-image)

## Medium Posts

- [Ctrl + c, Ctrl + v — Replicating Data Science Conda Environment](https://codenamewei.medium.com/ctrl-c-ctrl-v-replicating-data-science-conda-environment-c190ad0d93fd)
  - [Conda Commands Cheatsheet](miniconda-guidelines.md)
- [Displaying visuals with Markdown](https://medium.com/geekculture/displaying-visuals-with-markdown-c39f2495e146)
  - [Examples of displaying image in readme.md](https://github.com/codenamewei/pydata-science-playground/blob/main/notebooks/markdown/readme.md)
  - [Examples of displaying image in Jupyter](https://github.com/codenamewei/pydata-science-playground/blob/main/notebooks/markdown/markdown_guidelines.ipynb)
