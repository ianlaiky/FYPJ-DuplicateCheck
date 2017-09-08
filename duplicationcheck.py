import os
from openpyxl import load_workbook
import pandas as pd
import fnmatch
import re

# userWeb = input("Word duplication check: ")

# loading in workbook
wb = load_workbook('ner.xlsx')

print("Sheets names:")
# obtaining sheets names
print(wb.get_sheet_names()[0])
sheet = wb[wb.get_sheet_names()[0]]

#
data = sheet.values

# print(next(data)[0:])
columnlist =[]

numbersss = 0
for r in data:
    # print(r[0])
    columnlist.append(r[0])
    numbersss += 1
# print(columnlist)


# regex test


# for i in columnlist:
#     print(i)

for i in columnlist:
    try:
        if fnmatch.fnmatch(i,"*coll*"):
            print(i)

    except Exception:
        pass






print(numbersss)





