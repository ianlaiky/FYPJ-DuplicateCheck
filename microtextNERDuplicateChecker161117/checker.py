from openpyxl import load_workbook

import fnmatch


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
# col 1 to check
microTextEnglishFull=[]
microTextSinglishFull=[]
nerLocationFull=[]
nerOrganisationFull=[]
nerPeopleFull=[]
nerMiscellaneousFull=[]



microTextEnglishCol1=excelinput("dataFiles\Microtext.xlsx",2,0)
print(microTextEnglishCol1)
microTextEnglishCol2=excelinput("dataFiles\Microtext.xlsx",2,1)
print(microTextEnglishCol2)
microTextEnglishCol3=excelinput("dataFiles\Microtext.xlsx",2,2)
print(microTextEnglishCol3)
microTextEnglishFull.append(microTextEnglishCol1)
microTextEnglishFull.append(microTextEnglishCol2)
microTextEnglishFull.append(microTextEnglishCol3)
print(microTextEnglishFull)

microTextSinglishCol1=excelinput("dataFiles\Microtext.xlsx",0,0)
microTextSinglishCol2=excelinput("dataFiles\Microtext.xlsx",0,1)
microTextSinglishCol3=excelinput("dataFiles\Microtext.xlsx",0,2)
microTextSinglishFull.append(microTextSinglishCol1)
microTextSinglishFull.append(microTextSinglishCol2)
microTextSinglishFull.append(microTextSinglishCol3)

nerLocationCol1=excelinput("dataFiles\\NER.xlsx",5,3)
nerLocationCol2=excelinput("dataFiles\\NER.xlsx",5,0)
nerLocationCol3=excelinput("dataFiles\\NER.xlsx",5,1)

newnerLocationCol1=[]
newnerLocationCol2=[]
newnerLocationCol3=[]


# print(nerLocationCol1)


for index,ner1 in enumerate(nerLocationCol1):

    if str(ner1)!="None":

        newnerLocationCol1.append(nerLocationCol1[index])
        newnerLocationCol2.append(nerLocationCol2[index])
        newnerLocationCol3.append(nerLocationCol3[index])

nerLocationFull.append(newnerLocationCol1)
nerLocationFull.append(newnerLocationCol2)
nerLocationFull.append(newnerLocationCol3)

# print(nerLocationFull)
# print(nerLocationFull[0][57])
# print(nerLocationFull[1][57])
# print(nerLocationFull[2][57])


