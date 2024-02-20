import pandas as pd
import numpy as np
from io import StringIO
csv_data='''a,b,c,d
1.0,2.0,3.0,4.0
33.0,34.0,35.0,36.0
54.0,81.0,93.0
29.0,,22.0
43.0,,1.0'''

df=pd.read_csv(StringIO(csv_data))
print(df)
print("-----------------------------------")
print(df.isnull().sum())
print("-----------------------------------")

# Solution 1: Delete the whole row of missing value
print(df.dropna(axis=0));# axis=0 refers to deleting of row
print("-----------------------------------")

# Solution 2: Delete the whole column of missing values
print(df.dropna(axis=1))
print("-----------------------------------")

# Note: The above two methods of missing data handling has a limitation that the whole row or column has to be deleted and we could face a data loss.
# Therefore, Solution 3: Fill up the null values with mean/median/mode
from sklearn.impute import SimpleImputer
imr = SimpleImputer(missing_values=np.nan,strategy='most_frequent') 
imr=imr.fit(df.values)
imputed_data=imr.transform(df.values)
print(imputed_data)
print("-----------------------------------")
df1=pd.DataFrame(imputed_data,index=["0","1","2","3","4"],columns=["a","b","c","d"])
print(df1)
print("-----------------------------------")
# Solution 4: Fill-up the values with the mean of the data
df=df.fillna(df.mean())
print(df)
print("-----------------------------------")
# Solution 5: Fill-up the values with median.
df=df.fillna(df.median())
print(df)
print("-----------------------------------")