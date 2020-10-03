import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt


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
ex_one = two_d_array[0, 1]  # Gets the first row of the second column
ex_two = two_d_array[0]  # Gets a single row
ex_three = two_d_array[:, 2]  # Gets the entire age column

# Suppose we want requirements, let's mask some data:
mask_ex_one = ex_three < 18  # Gets the number of minors on the ship
# print(two_d_array[mask_ex_one])  # It needs to be plugged in to be a good mask

sum_of_children = mask_ex_one.sum()  # Returns 2

# Coding exercise
high_class_sum = (two_d_array[:, 0] == 1).sum()

# We can use scatter to plot our data
plt.scatter(df['Age'], df['Fare'], c=df['Pclass'])

# Set the X and Ys
plt.xlabel("Age")
plt.ylabel("Fare")

# And plot a line
plt.plot([0, 80], [85, 5])

# Required at the end to show the data.
plt.show()
