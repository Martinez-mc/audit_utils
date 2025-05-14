import pandas as pd

"""
Takes a QB GL in xlsx format and returns
a flat file.

TODO:
    A) Need to create one, and only one column for the account information.  
"""

# Load workbook
df0 = pd.read_excel('gl.xlsx', sheet_name='Sheet1')

# Replace uncommon character
df1 = df0.replace('·', '-', regex=True)

# Drop rows containing the word "Total"
indices_to_drop = df1[df1.apply(lambda row: row.astype(str).str.contains('total', case=False).any(), axis=1)].index
df = df1.drop(indices_to_drop)

# Perform forward fill in account columns
df[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3']] = df[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3']].ffill()

#Rename headers
df.rename(columns={'Unnamed: 1': 'Account1', 'Unnamed: 2': 'Account2', 'Unnamed: 3': 'Account3'}, inplace=True)

# Drop NaN rows from Type column
df = df.dropna(subset=['Type'])

# Drop unecessary columns
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 4', 'Balance'])

# Export to csv
df.to_csv('output_file.csv', index=False, header=True)

print(df.head())

