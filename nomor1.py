import numpy as np
import pandas as pd

data = {'Outlook': ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 
    'rainy', 'sunny', 'overcast', 'overcast', 'rainy'],
    'Temperature': [85, None, 83, None, 68, 65, None, 72, 69, 75, 75, 72, 81, 71],
    'Humidity': [85, 90, 86, 96, 80, None, 65, 95, 70, None, 70, None, 75, 91],
    'Windy': [False, True, False, False, False, True, True, False, False, False, True, True, False, True],
    'PlayTennis': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']}

df = pd.DataFrame(data)
df.to_csv("PlayTennis.csv")

num_missing_values = df.isna().sum().sum()
print("Jumlah record yang mengandung missing value:", num_missing_values)

df['Temperature'].fillna(df['Temperature'].mean(), inplace=True)
df['Humidity'].fillna(df['Humidity'].mean(), inplace=True)
print("DataFrame setelah diisi dengan mean:")


print(df)
