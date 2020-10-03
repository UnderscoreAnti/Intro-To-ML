import pandas as pd
import numpy as ny
import matplotlib as mpl


# Pandas reads the CSV files and coverts it into usable data
df = pd.read_csv('titanicdata.csv')

# This returns a table of statistics about each column
pd.options.display.max_columns = 6
# print(df.describe())

# This returns a single column, called a DATA SERIES
column = df["Fare"]
# print(column)

# And this returns a smaller data frame
small_df = df[["Age", "Survived", "Sex"]]
# print(small_df.head())

# This converts the sex values from strings to booleans
# df['male'] = df['Sex'] == 'male'

