import pandas as pd

df = pd.read_csv('data/processed/npci_declined_cleaned.csv')
print(df['date'].unique())
print("\nTotal unique dates:", df['date'].nunique())
