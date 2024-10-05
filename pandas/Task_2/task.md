# Task_1: 
## Use for yourself dataset.csv document but <br><br>`DO NOT FORGET TO GET RID OF DATASET.CSV FROM THE FUNCTION` 
1. In the function `read_and_return_specific_column` you should write code to read .csv file and return its specific 'platfrom' column as DataFrame. Do not forget that DataFrame is separately pandas.Series.
2. In `read_and_set_index` your function should read .csv file and set as index the `'genre'` column and return the result.
3. In `read_and_rename_column` your function should read .csv file and rename `'platform'` column to `'device'`, then return the resulting DataFrame.
4. In `read_and_valuecount` your function should read .csv file and count the frequency of values on the column `'platform'` and return the result as DataFrame.
5. In `read_and_sortvalues` your function should read .csv file and sort its values by column `'genre'` and return the result.
6. In `read_and_return_specific_info` your function should read .csv file and return DataFrame where on column `'platform'` there is only `'PS4'` value (you might want to use index for DataFrame like df[] and use boolean expression in brackets).
7. In `read_and_return_concatenation` your function should read .csv file and return concatination of 2 DataFrames where in first one there is only `PS4` and in the second one only `'XOne'` as the value for column `'platform'` (Use pandas function `pd.concat()` for concatenation of DataFrames).
#### For more information about the function calls for [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) or [Pandas user-guide](https://pandas.pydata.org/docs/user_guide/index.html)