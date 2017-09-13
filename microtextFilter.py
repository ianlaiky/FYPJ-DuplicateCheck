import re
from openpyxl import load_workbook
from collections import Counter


def excelinput(filetoeopn, filecheckksheets, columnNo):
    columnlist = []
    # loading in workbook
    wb = load_workbook(filetoeopn)

    print("Sheets names:")
    # obtaining sheets names
    print(wb.get_sheet_names())
    sheet = wb[wb.get_sheet_names()[filecheckksheets]]

    #
    data = sheet.values

    for r in data:
        # print(r[0])
        if r[columnNo] is not None:
            # print(r[columnNo])
            columnlist.append(r[columnNo])

    return columnlist


# excelinput("datafiles\sgforums.xlsx",0,0)


class DataValue():
    def __init__(self, itemm, countt):
        self.item = itemm
        self.count = countt

    def getitem(self):
        return self.item

    def getitemCount(self):
        return self.countt

    def setitemCounr(self, itemm):
        self.item = itemm
        return self.item


tempppppaarrrrr = []


def wordduplicationcheck(wordstocheck):
    tempppppaarrrrr.append(wordstocheck)


f = open('test.txt', 'w', encoding="utf-8")

counttttt = 0

for i in excelinput("datafiles\sgforums.xlsx", 0, 0):
    # print(i)
    print("Currently scanning Line: " + str(counttttt))
    counttttt = counttttt + 1
    i = str(i).replace('\n', " ")
    i = str(i).replace('\\n', " ")
    i = str(i).lower()
    # do blank check to see if have space
    if str(i).find(" ") != -1:
        for x in re.split(" |,", i):
            # print(x)
            # f.writelines(x+"\n")
            wordduplicationcheck(str(x).strip())
    else:
        wordduplicationcheck(str(i).strip())

my_dict = Counter(tempppppaarrrrr)

del my_dict[' ']
del my_dict['']

for fg in my_dict:
    f.writelines(fg + "\t\t" + str(my_dict[fg]) + "\n")
print("Done")

f.close()
