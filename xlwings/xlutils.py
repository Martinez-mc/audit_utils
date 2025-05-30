

# Import libraries as needed
import xlwings as xw
from xlwings import constants, Range
from datetime import datetime
import pandas as pd
import pyperclip

# (Live book) Works on the active app, book, sheet 
# Lets you interact with any open book without fully qualifying path.
app = xw.apps.active
wb = app.books.active
sht = wb.sheets.active

rng = Range("W8:W4736")

for cell in rng:
    if cell.offset(column_offset=-4).value > 365:
        if cell.offset(column_offset=-2).value > 0 or cell.offset(column_offset=-2).value < 0:
            cell.value = 0
            print(cell.address)
        elif cell.offset(column_offset=-1).value > 0 or cell.offset(column_offset=-1).value < 0:
            cell.value = 0
            print(cell.address)

    else:
        cell.value = cell.offset(column_offset=-3).value
        print(cell.address)

        
















# Snippets
"""
sht.range('B2').value = str(sht.range('B2').value).title()
sht.range('B3').value = str(sht.range('B3').value).title()
sht.range('B4').value = str(sht.range('B4').value).title()
"""

""" 
# Loop as you would normally do
for cell in sht.range('A2:A10'):
    print(cell.value)
 """

""" 
# See if a cell is empty
for cell in sht.range('A2:A10'):
    if cell.value == None:
        cell.value = "Hello"
 """

""" 
# Offset
# Lets say you want to copy a cell (range) into an adjacent cell.
# offset(row, column)
# row positive number will move down.
# row negative number will move up.
# column positive number will move right
# column negative number will move to left.

for cell in sht.range('C2:C10'):
    cell.offset(0, -1).value = cell.value 
"""

"""
rng = Range('C9:C156')

for x in rng:
    if x.api.Font.Bold == True:
        x.offset(row_offset=1, column_offset=-2).value = x.value 
        x.offset(row_offset=1, column_offset=-1).value = x.offset(row_offset=0, column_offset=1).value
        print(x.address)

"""

""" 
# Perform a forward fill
# Gap Filler
for cell in sht.range('A2:A20'):
    if cell.value == None:
        cell.value = cell.offset(-1, 0).value
"""

""" 
# In case you want to test if the cell content
# starts with a number.
for cell in sht.range('A1:A10'):
    if cell.value[0].isdigit():
        print(cell.value)
    else:
        print("Does not start with a number")

# This will get more interesting if regular expressions
# used.
 """
""" 
# Sometimes you would want to clear a cell based
# on its contents.
#Cell Deleter
for cell in sht.range('A1:A10'):
    if cell.value[0].isdigit():
        print(cell.value)
    else:
        cell.value = None
 """

# Save and close if needed.
# wb.save() 
# # wb.close()