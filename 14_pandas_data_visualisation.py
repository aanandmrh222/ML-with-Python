import pandas as pd
data=pd.read_csv("Salaries.csv")
print(data)
print(data.shape)
print(data.head(20))# head function gives us the starting rows of the dataset
print(data.tail(5))# tail function gives us last rows from the dataset
print(data.dtypes)# to know the datatypes of the columns
print(data['salary'].dtypes)# knowing datatype of a particular column
# DataFrame Attributes
'''dtypes, columns, axes, ndim, size, shape, values, shape'''
print(data.columns)
print(data.size)
print(data[2:78])
'''DataFrame Methods:
   -> head() / tail()
   -> describe()
   -> max() / min()
   -> mean() / median()
   -> std(): Standard deviation
   -> sample([n])
   -> dropna():drop records with missing values
'''
print(data.describe())
print(data.mean())
print(data.head(50).mean(numeric_only=all))