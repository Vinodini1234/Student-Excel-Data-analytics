import pandas as pd
import numpy as np
disease=["Flu","Cold","Malaria","Dengue","Tuberculosis"]
patient_count=[100,150,50,30,20]
data={"Disease":disease,"Patient Count":patient_count}
df=pd.DataFrame(data)
print(df)
print("\nTotal number of patients:", df["Patient Count"].sum())
print("\nAverage number of patients per disease:", np.mean(patient_count))
print("\nDisease with the highest patient count:", df.loc[np.argmax(df["Patient Count"]), "Disease"])
print("\nDisease with the lowest patient count:", df.loc[np.argmin(df["Patient Count"]), "Disease"])
print("\nPercentage of patients for each disease:")
df["Percentage"] = (df["Patient Count"] / df["Patient Count"].sum()) * 100
print(df[["Disease", "Percentage"]])
print("Correlation between diseases and patient count:", np.corrcoef(df["Patient Count"], np.arange(len(df))))