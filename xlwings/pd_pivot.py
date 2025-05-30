import numpy as np
import pandas as pd

df = pd.read_clipboard()
pvt = pd.pivot_table(df,
                     index=['Invoice Number', 'Invoice Date', 'Nombre Proveedor'],
                     aggfunc={"Open Amount": np.sum})

pvt.to_excel('Pivot.xlsx')