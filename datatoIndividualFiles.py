import re
from openpyxl import load_workbook

def excelinput(filetoeopn, filecheckksheets, columnNo):
    columnlist = []
    # loading in workbook
    wb = load_workbook(filetoeopn)

    print("Sheets names:")
    # obtaining sheets names
    print(wb.get_sheet_names())
    print("Sheets Loaded: " + wb.get_sheet_names()[filecheckksheets])
    sheet = wb[wb.get_sheet_names()[filecheckksheets]]

    #
    data = sheet.values

    # print(next(data)[0:])

    for r in data:
        # print(r[0])
        columnlist.append(r[columnNo])

    return columnlist

counttttt = 0

currentFileNo=0

for i in excelinput("datafiles\sgforums.xlsx", 0, 0):
    if str(i) != "None":

        print("Currently scanning Line: " + str(counttttt))
        counttttt = counttttt + 1
        i = str(i).replace('\n', " ")
        i = str(i).replace('\\n', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")
        i = str(i).replace('', " ")

        i = str(i).replace('…', '...')
        print(i)

        f = open("../sentencesInFiles\sentence_"+str(currentFileNo)+".txt","w", encoding="utf-8")
        f.writelines(str(i))
        f.close()
        currentFileNo=int(currentFileNo)+1