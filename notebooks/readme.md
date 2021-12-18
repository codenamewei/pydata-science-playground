## Data Structure 

### List 
- List of str to int: ```list(map(int, arr))```
- Split str to list of str: ```arr.split(" ")```
- Sort an array in place: ```arr.sort()```
- Get index of a value: ```arr.index(value)```

### Dictionary
- Get keys as list: ```list(lut.keys())```
- Get values as list: ```list(lut.values())```
- Create dict from list: ```{i: 0 for i in arr}```
- Find if key exists in existing dict: ```if k in lut```
- Save/load dictionary to/from a file: [saveloaddict.ipynb](dictionary/saveloaddict.ipynb)

## Math
- Define Nan, Infinite: [define_nan_infinite.ipynb](math/define_nan_infinite.ipynb)
- Sum up an array: ```sum(arr)```
- Round up a number to a certain decimal point: ```round(value, 1)``` 

## File System
- Iterate through a path to get files/folders : [filesystem/os_walk.ipynb](filesystem/os_walk.ipynb)
- Check if path exist: ```os.path.exists('designated_path')```

## String
- Check file extension: [string/check_file_extension.ipynb](string/check_file_extension.ipynb)

## Numpy
- Numpy NaN (Not A Number): Constant to act as a placeholder for any missing numerical values in the array: ```np.NaN / np.nan / np.NAN```

## [Pandas](https://pandas.pydata.org/docs/reference/)

- Sort rows: ```df.sample(frac=1)```
- Create new column and assign value according to another column - tbd

- Referring to dataframe column by key or by string: [refer_column_name.ipynb](pandas/refer_column_name.ipynb)

- Get subset of dataframe, sample columns with specific criteria: [sample_df.ipynb](pandas/sample_df.ipynb)
    - Sample by percentage
    - Sample by # of rows specified
    - Sample by matching to a value
- Concatenate dataframe: [concat_df.ipynb](pandas/concat_df.ipynb)
    - Concatenate by adding rows
- Drop rows/columns with np.NaN: ```df3 = df3.dropna(axis = 0) #column```

### Infos
- [Dataframe basic](pandas/info_basic.ipynb)
    - Get # rows and columns
    - Get summary/infos about dataframe
= [Get data types](pandas/column_types.ipynb)
- [Dataframe/Series Min, Max, Median, General Description](pandas/series_min_max.ipynb)
- [Get rows name (index) and columns name (column)](pandas/info_rows_columns.ipynb)
- [Get a glimpse of dataframe](pandas/info_glimpse.ipynb)
- [Get subset of a dataframe by rows/by columns](pandas/df_subset.ipynb)
- [Get rows by finding matching values from a specific column](pandas/df_find_rows.ipynb)

### Change type
- [Series to value](pandas/series_to_values.ipynb)
- Series to numpy array - ```input.to_numpy()```
- [Change column type](pandas/change_column_type.ipynb)
- [Rename column name if exist](pandas/rename_column.ipynb)

### Assign values
- [Dataframe append columns](pandas/df_append_column.ipynb)
- Dataframe append rows - tbd

- Assign values by index
- Assign values by lambda - tbd - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html

### Remove/drop values
- [Drop duplicates](pandas/drop_duplicate.ipynb)
- [Remove/drop rows where specific column matched value](pandas/remove_with_matching_value.ipynb)
- [Remove specific columns with column name](pandas/remove_column.ipynb)

### Excel like functions
- pivot table - tbd
- group by - tbd

### CSV In/Out
- Save to csv ```df.to_csv('file name', index = False```
    - Note: Put ```index = False``` is important to prevent an extra column of index being saved.

### Excel In/Out
- Read in excel as a whole, get sheet names
- Read in excel with speciic sheet name
- Save excel ```df.to_excel('file_name', index = False) ```

### Loc
- Find rows based on specific column(s) matching value - ```df.loc[df['address'].eq('johndoe@gmail.com')]```
- [Assign value to specific column(s) by matching value](pandas/df_assign_col_values.ipynb)

### Iloc 
- Get a subset of dataframe by rows - ```df.iloc[<from_rows>:<to_rows>, :]```


## Pytorch

- Check if cuda is available - ```import torch; torch.cuda.is_available()``` 


## Huggingface

- Send model to cuda - ```model = model.to('cuda:0')```
