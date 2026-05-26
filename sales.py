import pandas as pd
import numpy as np
items=["Book","Pen","Pencil","Eraser","Sharpener"]
items_count=[10,20,15,5,8]
sold=[5,15,10,3,6]
data={"Items":items,"No.of_Items":items_count,"Sold":sold}
df=pd.DataFrame(data)
print(df)
print("\nTotal number of items:",df["No.of_Items"].sum())
print("Total number of items sold:",df["Sold"].sum())
print("\nAverage number of items sold per item:",np.mean(sold))
print("Standard deviation of items sold:",np.std(sold))
print("\nItems with more than 10 sold:")
print(df[df["Sold"] > 10])
print("\nItems with less than 5 sold:")
print(df[df["Sold"] < 5])
print("\nPercentage of items sold:")
df["Percentage_Sold"] = (df["Sold"] / df["No.of_Items"]) * 100
print(df[["Items", "Percentage_Sold"]])
print("relationship between number of items and sold:",np.corrcoef(items_count, sold))
