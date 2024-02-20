# Handling Categorical Data
import pandas as pd
import numpy as np
df = pd.DataFrame([
['green', 'M', 10.1, 'class2'],
['red', 'L', 13.5, 'class1'],
['blue', 'XL', 15.3, 'class2'],
['Yellow',"S",34.6,"class3"]])
df.columns = ['color', 'size', 'price', 'Label']
print(df)
print("----------------------------------------")
# Data Mapping
size_mapping={'XL':2,'L':1,'M':0,'S':3}
df['size']=df['size'].map(size_mapping)
print(df)
print("----------------------------------------")
# Data Inverse Mapping
inv_size_mapping={v:k for k,v in size_mapping.items()}
print(df['size'].map(inv_size_mapping))
print("----------------------------------------")
df['size']=df['size'].map(inv_size_mapping)
print(df)
print("----------------------------------------")

#Data Encoding (Enumerate)
class_mapping={label:idx for idx,label in enumerate(np.unique(df['Label']))}
print(class_mapping)
print("----------------------------------------")
df['Label']=df['Label'].map(class_mapping)
print(df)
print("----------------------------------------")
inv_class_mapping={v:k for k,v in class_mapping.items()}
print(inv_class_mapping)
print("----------------------------------------")
df['Label']=df['Label'].map(inv_class_mapping)
print(df)
print("----------------------------------------")