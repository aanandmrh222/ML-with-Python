import pandas as pd
import numpy as np

df = pd.read_csv("Salaries.csv")

# print(df)
# print(df.shape)
# print(df.head(10))
# print(df.tail(20))
# print(df.dtypes)
# print(df['salary'].dtypes)

# data frames attributes
# dtypes, columns, axes, ndim, size, shape, values 

# print(df.columns)     # to display all columns in data fames

# data fames method
# head/ tail(), describe(), max() / min(), mean/median, std(), sample([n]), dropna()

# print(df.describe())
# print(df.mean())
# ak = (df.head(50)).mean(numeric_only = all)
# print(ak)


# df_mean = df.head(50)
# print(df.mean.mean())
# print(df.mean())

# print(df['salary'].describe())

# print(df['salary'].count())

# print('AVG SAL: ',df['salary'].mean())

df_rank = df.groupby(['rank'])
print(df_rank)