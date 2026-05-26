import pandas as pd
import numpy as np
Marks=[85, 90, 92, 78, 82, 88]
Study_hrs=[5, 6, 7, 4, 5, 6]
data={'Marks':Marks,'Study_hrs':Study_hrs}
df=pd.DataFrame(data)
print(df)
print(df.describe())
print(df.corr())
print(df['Marks'].mean())
print(df['Study_hrs'].mean())
print(df['Marks'].std())
print(df['Study_hrs'].std())
print(df['Marks'].min())
print(df['Marks'].max())