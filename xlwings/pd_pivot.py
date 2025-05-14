import numpy as np
import pandas as pd

df = pd.read_clipboard()
pvt = pd.pivot_table(df,
                     index=["Id)", "Check Date","Supplier Number", "Invoice Number"],
                     aggfunc={'Payment Amount': np.sum})

pvt.to_excel('Pivot.xlsx')