# Working with `pandas` library
## Now we will learn how to use `pandas` dataframe and what we can do with it.
#### -To create DataFrame we use `pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)`, where:
1. `data` is your table or other type of information,
2. `index` what column you want to make as index,
3. `columns` what columns are there,
4. `dtype` what type of data,
5. `copy` to copy inputs or not.

Example of creating DataFrame:<br>
`d = {'col1': [1, 2], 'col2': [3, 4]}`  
`df = pd.DataFrame(data=d)`
#### -DataFrame actually has its own functions as well, some of them are:
`.set_index()` - to set index using existing columns<br>
`.sort_values()` - sort by the values along their axes<br>
`.reset_index()` - reset the index <br>
`.rename()` - rename columns or indexes<br>
`.value_counts()` - returns series with the frequency of each distinct row<br>
more on [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

### -How to use these functions with examples:
#### 1. `pandas.DataFrame.set_index(keys, *, drop=True, append=False, inplace=False, verify_integrity=False)`
`keys`: label or array-like or list of labels/arrays which indicate what shall be index<br>
`drop`: boolean which indicates whether to delete columns to be used as the new index<br>
`append`: boolean which indicates whether to append columns to existing index<br>
`inplace`: boolean which indicates whether to modify DataFrame rather than creating a copy<br>
`verify_integrity`: boolean indicates whether to check the nex index for duplicates<br>
`Return` types are: `DataFrame` or `None` if `inplace=True`.<br>

Example:<br>
`df = pd.DataFrame({'month': [1, 4, 7, 10],`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`'year': [2012, 2014, 2013, 2014],`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`'sale': [55, 40, 84, 31]})`<br>
`df`<br>
   &ensp;`month  year  sale`<br>
`0      1  2012    55`<br>
`1      4  2014    40`<br>
`2      7  2013    84`<br>
`3     10  2014    31`<br>
##### Set the index to become the ‘month’ column:
`df.set_index('month')`<br>
`month      year  sale`<br>
`1      2012    55`<br>
`4      2014    40`<br>
`7      2013    84`<br>
`10     2014    31`<br>
##### Create a MultiIndex using columns ‘year’ and ‘month’:
`df.set_index(['year', 'month'])`<br>
            
`year  month sale`<br>
`2012  1     55`<br>
`2014  4     40`<br>
`2013  7     84`<br>
`2014  10    31`<br>

#### 2. `pandas.DataFrame.sort_values(by, *, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)`
`by`: string ot list of strings which is name or names to sort by<br>
`axis`: 0 or 'index', 1 or 'columns' which is what axis to be sorted<br>
`ascending`: boolean or list of boolean to sort ascending or descending<br>
`inplace`: boolean which indicates whether to modify DataFrame rather than creating a copy<br>
`kind`: ‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’ - choice of sorting algorithm<br>
`na_position`: ‘first’, ‘last’ - to put NaN values first or last<br>
`ignore_index`: boolean to indicate to leave index or not<br>
`key`: *callable,optional* - to apply key function before sorting the values<br>
`Return` types are: `DataFrame` or `None` if `inplace=True`.<br>
Example:<br>
`df = pd.DataFrame({`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`'col2': [2, 1, 9, 8, 7, 4],`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`'col3': [0, 1, 9, 4, 2, 3],`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`'col4': ['a', 'B', 'c', 'D', 'e', 'F']})`<br>
<br>
`df`<br>
`  col1  col2  col3 col4`<br>
&ensp;&ensp;`0    A     2     0    a`<br>
&ensp;&ensp;`1    A     1     1    B`<br>
&ensp;&ensp;`2    B     9     9    c`<br>
&ensp;&ensp;`3  NaN     8     4    D`<br>
&ensp;&ensp;`4    D     7     2    e`<br>
&ensp;&ensp;`5    C     4     3    F`<br>
<br>
##### Sort values by `col1`
`df.sort_values(by=['col1'])`<br>
  `col1  col2  col3 col4`<br>
&ensp;&ensp;`0    A     2     0    a`<br>
&ensp;&ensp;`1    A     1     1    B`<br>
&ensp;&ensp;`2    B     9     9    c`<br>
&ensp;&ensp;`5    C     4     3    F`<br>
&ensp;&ensp;`4    D     7     2    e`<br>
&ensp;&ensp;`3  NaN     8     4    D`<br>

#### 3. `pandas.DataFrame.reset_index(level=None, *, drop=False, inplace=False, col_level=0, col_fill='', allow_duplicates=<no_default>, names=None)`
`level`: integer,string,tuple or list for indicating what levels to remove<br>
`drop`: boolean to reset the index to the default integer index<br>
`inplace`: boolean which indicates whether to modify DataFrame rather than creating a copy<br>
`col_level`: integer or string to if columns have levels determine which level the labels are inserted into<br>
`col_fill`: object to be used for filling other levels' names of columns<br>
`allow_duplicates`: boolean, *optional* to allow duplicate column labels to be created <br>
`names`: integer, string or 1-dimensional list to rename column which contains the index data<br>
`Return` types are: `DataFrame` with new index or `None` if `inplace=True`.<br>
Example:<br>
`df.set_index('month')`<br>
`month      year  sale`<br>
`1      2012    55`<br>
`4      2014    40`<br>
`7      2013    84`<br>
`10     2014    31`<br>
<br>
`df.reset_index()`<br>
&ensp;`month      year  sale`<br>
`0 1      2012    55`<br>
`1 4      2014    40`<br>
`2 7      2013    84`<br>
`3 10     2014    31`<br>

#### 4. `pandas.DataFrame.rename(mapper=None, *, index=None, columns=None, axis=None, copy=None, inplace=False, level=None, errors='ignore')`
`mapper`: dict-like or function transformations to apply to that axis' values<br>
`index`: dict-like or function which is alternative to specify axis<br>
`columns`: dict-like or function which is alternative specify axis<br>
`axis`: 0 or 'index', 1 or 'columns' which is axis to target with `mapper`<br>
`copy`: boolean to also copy underlying data <br>
`inplace`: boolean which indicates whether to modify DataFrame rather than creating a copy<br>
`level`: integer or level name to use if multiindex, only rename labels in the specified level<br>
`errors`: ‘ignore’, ‘raise’ to check and fix errors or not<br>
`Return` types are: `DataFrame` with renamed axis labels or `None` if `inplace=True`.<br>
Example:<br>
`df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})`<br>
##### Rename columns 
`df.rename(columns={"A": "a", "B": "c"})`<br>
&ensp;&ensp;`a  c`<br>
`0  1  4`<br>
`1  2  5`<br>
`2  3  6`<br>
##### Rename index 
`df.rename(index={0: "x", 1: "y", 2: "z"})`<br>
&ensp;&ensp;`A  B`<br>
`x  1  4`<br>
`y  2  5`<br>
`z  3  6`<br>

#### 5. `pandas.DataFrame.value_counts(subset=None, normalize=False, sort=True, ascending=False, dropna=True)`
`subset`: label of list of labels, *optional* which is columns to use when counting unique combinations<br>
`normalize`: boolean whether to return propositions rather than frequencies<br>
`sort`: boolean whether to sort by frequencies(True) or by column values(False)<br>
`ascending`: boolean whether to sort in ascending order<br>
`dropna`: boolean whether to include counts of rows that contain NA values <br>
`Return` type: `Series`.<br>
Example:<br>
`df = pd.DataFrame({'num_legs': [2, 4, 4, 6],`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`'num_wings': [2, 0, 0, 0]},`<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`index=['falcon', 'dog', 'cat', 'ant'])`<br>
`df`<br>
<br>
&ensp;&ensp;&ensp;`num_legs  num_wings`<br>
`falcon      `&ensp;&ensp;`   2         2`<br>
`dog       `&ensp;&ensp;&ensp;&ensp;&ensp;`      4          0`<br>
`cat        `&ensp;&ensp;&ensp;&ensp;&ensp;`     4          0`<br>
`ant         `&ensp;&ensp;&ensp;&ensp;&ensp;`    6          0`<br>
##### Use value_counts()
`df.value_counts()`<br>
`num_legs  num_wings`<br>
&ensp;&ensp;&ensp;`4    `&ensp;&ensp;&ensp;&ensp;&ensp;`      0       `&ensp;&ensp;&ensp;&ensp;&ensp;`      2`<br>
&ensp;&ensp;&ensp;`2     `&ensp;&ensp;&ensp;&ensp;&ensp;`     2         `&ensp;&ensp;&ensp;&ensp;&ensp;`    1`<br>
&ensp;&ensp;&ensp;`6      `&ensp;&ensp;&ensp;&ensp;&ensp;`    0          `&ensp;&ensp;&ensp;&ensp;&ensp;`   1`<br>
`Name: count, dtype: int64`<br>



<br>These functions we will be using for analyzing our DataFrame and for each of them you will be doing tasks and after all you will be able to make ready DataFrame to plot.

                