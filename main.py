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

# This creates a new column: Male = True, Female = False
df['Male'] = df['Sex'] == 'male'

# This method creates a 1 Dimensional Array
one_d_array = df[['Fare']].values
# print(one_d_array)

# This method creates a 2 Dimensional Array
two_d_array = df[["Pclass", "Fare", "Age"]].values[:10]

# We can look at the shape of the array in rows and columns
two_d_arr_shape = two_d_array.shape
# print(two_d_arr_shape)

# Just for the sake of computational science, remember:
ex_one = two_d_array[0, 1]  # Gets the second row of the first column
ex_two = two_d_array[0]  # Gets a single row
ex_three = two_d_array[:, 2]  # Gets the entire age column

# Suppose we want requirements, let's mask some data:
mask_ex_one = ex_three < 18
print(two_d_array[mask_ex_one])

