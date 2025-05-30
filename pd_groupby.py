import pandas as pd

df = pd.read_clipboard()
grouped = df.groupby('Nombre Proveedor').agg({
    'Invoice Number': lambda x: list(x)
})
print(grouped)