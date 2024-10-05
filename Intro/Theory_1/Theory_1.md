# Set-up libraries we will need

We will have to import several libraries for reading, analyzing and plotting the [data](jetbrains://pycharm/navigate/reference?project=Python Project&path=Data/dataset.csv) we have.
We need these three libraries:
- [Seaborn](https://seaborn.pydata.org/) : Mainly used for plotting and visualizing data after analyzing.
- [Pandas](https://pandas.pydata.org/) : Used for analyzing data and making the datasets.
- [Matplotlib](https://matplotlib.org/) : Also used for plotting and analyzing data, however, in our project we will not focus on this library(rather on matplotlib.pyplot).

## To import labraries we can:
1. Simply import: `import seaborn` 
2. Import needed module from library: `import matplotlib.pyplot` or `import pyplot from matplotlib`
3. Import library and add `as`: `import pandas as pd`

We will be using third way to set up all libraries and these libraries are recommended to be imported like:\
`import seaborn as sns`\
`import pandas as pd`\
`import matplotlib.pyplot`

## Now we will upload data from .csv file
We have several ways to read data in python, but our data is .csv type and pandas has the most suitable function for reading from such files, where data is separated with coma
`pandas.read_csv("name_of_csv_file")`

So, we type `pd.read_csv("dataset.csv")` to read the data and to be able to use it,
we shall assign it to a variable like:`data = pd.read_csv("dataset.csv")`

After assigning the data, it is saved as Pandas Dataframe which is actually just a table but with its own limitations.
You can check it by typing `type(data)`, this type of data has several functions which can be called, like to show first five or last five rows as:
`data.head()` or `data.tail()`.

Also, if you want to change the type of your variables like from integer to a string, you may use shortcut like `str(integer)`.

### Now you may go to the task and make it to the next lesson



