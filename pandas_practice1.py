import numpy as np
#import pandas library to use pandas functions
import pandas as pd
#To generate random number
from numpy.random import randn

np.random.seed(101)

#The pd. DataFrame takes arguments as data,index, columns
#the rnadn function arguments are in the order of number of rows and number of columns
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

print(df)

#Output as below, note the number of rows and columns, index, and column labels.
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

#Print the type of df to understand the datatype of the structure

print(type(df))
#Output
# <class 'pandas.core.frame.DataFrame'>

#Access the columns by mentioning the column name within quotes inside square brackets
print(df['W'])

#Output
# A    2.706850
# B    0.651118
# C   -2.018168
# D    0.188695
# E    0.190794
# Name: W, dtype: float64

#Accessing multiple columns, pass the column labels as list
print(df[['Y','Z']])

#Output
#      Y         Z
# A  0.907969  0.503826
# B -0.848077  0.605965
# C  0.528813 -0.589001
# D -0.933237  0.955057
# E  2.605967  0.683509

print(type(df[['Y','Z']]))
# Output
# <class 'pandas.core.frame.DataFrame'>
#note when multiple columns are returned, they are returned as type dataframe, however single columns are returned as type series


#To add new column as a product/ sum of other existing columns 
df['new_col'] = df['Y'] + df['Z']

print(df)
#Output
#      W         X         Y         Z   new_col
# A  2.706850  0.628133  0.907969  0.503826  1.411795
# B  0.651118 -0.319318 -0.848077  0.605965 -0.242112
# C -2.018168  0.740122  0.528813 -0.589001 -0.060187
# D  0.188695 -0.758872 -0.933237  0.955057  0.021819
# E  0.190794  1.978757  2.605967  0.683509  3.289476

#To drop a column, use the drop function , pass the column name as arguments, along with axis, 1 for columns and 0 for rows
#use the inplace parameter as true if you want the changes to stay in the main dataframe as False.
df.drop('new_col', axis=1, inplace=True)
print(df)

#output
#   W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

#To drop a row, use the drop function and pass the row label, axis is default to 0
df.drop('E', inplace=True)
print(df)

#Output: Note the row E is now dropped
#   W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057

#Selecting the row/column through labels and Indicies
#Rows by labels
print(df.loc['B'])

#Output
# W    0.651118
# X   -0.319318
# Y   -0.848077
# Z    0.605965
# Name: B, dtype: float64

print(df.iloc[1])

# W    0.651118
# X   -0.319318
# Y   -0.848077
# Z    0.605965
# Name: B, dtype: float64

#Selecting values based off the combination of rows and columns

print(df.loc['B','Y'])
#Output
# -0.8480769834036315

#Selecting values based of multiple rows and columns, pass the rows and columns as seperate lists

print(df.loc[['A','B'],['W','Y']])

#Output
#           W         Y
# A  2.706850  0.907969
# B  0.651118 -0.848077