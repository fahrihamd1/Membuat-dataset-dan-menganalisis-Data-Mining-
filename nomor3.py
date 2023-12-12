import pandas as pd
from efficient_apriori import apriori

df = pd.read_csv('Belanja.csv')

transactions = [item.split(", ") for item in df['Barang yang Dibeli']]

itemsets, rules = apriori(transactions, min_support=0.2, min_confidence=0.8)

for j in range(1, len(itemsets) + 1):
    print(itemsets[j])
    print("\n")

for rule in rules:
    print(rule)