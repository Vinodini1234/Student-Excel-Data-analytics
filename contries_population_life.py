import pandas as pd
import numpy as np
places=['India', 'United States', 'Brazil', 'Russia', 'United Kingdom', 'France', 'Spain', 'Italy', 'Germany', 'Turkey']
population=[1380004385, 331002651, 212559417, 145934462, 67886011, 65273511, 46754778, 60461826, 83783942, 84339067]
life_expectancy=[69.66, 78.93, 75.88, 72.58, 81.40, 82.66, 83.40, 83.51, 81.33, 77.69]
health_expenditure=[3.54, 16.89, 9.16, 5.35, 10.00, 11.26, 9.16, 8.83, 11.25, 4.28]
data = {'Place': places, 'Population': population, 'Life Expectancy': life_expectancy, 'Health Expenditure': health_expenditure}
df = pd.DataFrame(data)
print(df)
print("\nSummary Statistics:")
print(df.describe())
print("\nCorrelation Matrix:")
print(np.corrcoef(df['Life Expectancy'], df['Health Expenditure']))
print("average life expectancy:", np.mean(life_expectancy))
print("average health expenditure:", np.mean(health_expenditure))
print("median life expectancy:", np.median(life_expectancy))
print("median health expenditure:", np.median(health_expenditure))
print("standard deviation of population:",np.std(population))