import os
from openpyxl import load_workbook
# Retrieve current working directory (`cwd`)
# cwd = os.getcwd()
#
# print(cwd)
#
# print(os.listdir('.'))




#
# # Import pandas
# import pandas as pd
#
# # Assign spreadsheet filename to `file`
# file = 'ner.xlsx'
#
# # Load spreadsheet
# xl = pd.ExcelFile(file)
#
# # Print the sheet names
# print(xl.sheet_names)
#
# # Load a sheet into a DataFrame by name: df1
# df1 = xl.parse('NER')


#loading in workbook
wb = load_workbook('ner.xlsx')

print("Sheets names:")
#obtaining sheets names
print(wb.get_sheet_names())
