import xlsxwriter
from openpyxl import load_workbook
from collections import Counter



filesToReadList=[]
filesToReadList.append("dataFiles\\Microtext.xlsx,2,0,1,2")
filesToReadList.append("dataFiles\\Microtext.xlsx,0,0,1,2")
filesToReadList.append("dataFiles\\NER.xlsx,5,3,0,1")
filesToReadList.append("dataFiles\\NER.xlsx,6,3,0,1")
filesToReadList.append("dataFiles\\NER.xlsx,7,3,1,2")
filesToReadList.append("dataFiles\\NER.xlsx,8,3,1,2")

# tempcurrSheet=""

def excelinput(filetoeopn, filecheckksheets, columnNo):
    columnlist = []
    # loading in workbook
    wb = load_workbook(filetoeopn)

    print("Sheets names:")
    # obtaining sheets names
    print(wb.get_sheet_names())
    print("Sheets Loaded: " + wb.get_sheet_names()[int(filecheckksheets)])
    sheet = wb[wb.get_sheet_names()[int(filecheckksheets)]]
    # tempcurrSheet=str(sheet)

    #
    data = sheet.values

    # print(next(data)[0:])

    for r in data:

        if str(r) != "":
            if str(r) != " ":
                # print(r[0])
                columnlist.append(str(r[int(columnNo)]))

    return columnlist

arrayOfFilesData=[]

for readfiles in filesToReadList:
    wb = load_workbook(str(readfiles).strip().split(",")[0])
    print(wb.get_sheet_names()[int(str(readfiles).strip().split(",")[1])])
    print(str(readfiles).strip().split(",")[0])
    print(str(readfiles).strip().split(",")[1])
    print(str(readfiles).strip().split(",")[2])
    print(str(readfiles).strip().split(",")[3])
    print(str(readfiles).strip().split(",")[4])
    colAbbr=excelinput(str(readfiles).strip().split(",")[0],str(readfiles).strip().split(",")[1],str(readfiles).strip().split(",")[2])
    colFullForm=excelinput(str(readfiles).strip().split(",")[0],str(readfiles).strip().split(",")[1],str(readfiles).strip().split(",")[3])
    colPolar=excelinput(str(readfiles).strip().split(",")[0],str(readfiles).strip().split(",")[1],str(readfiles).strip().split(",")[4])

    sheetnames=wb.get_sheet_names()[int(str(readfiles).strip().split(",")[1])]

    FinalcolAbbr=[]
    FinalcolFullForm=[]
    FinalcolcolPolar=[]
    FinalSheetName=[]

    for index,checkcol in enumerate(colAbbr):
        if str(checkcol)!="":
            if str(checkcol)!=" ":
                FinalcolAbbr.append(str(colAbbr[index]))
                FinalcolFullForm.append(str(colFullForm[index]))
                FinalcolcolPolar.append(str(colPolar[index]))
                FinalSheetName.append(str(sheetnames))

    arrayOfFilesData.append(FinalcolAbbr)
    arrayOfFilesData.append(FinalcolFullForm)
    arrayOfFilesData.append(FinalcolcolPolar)
    arrayOfFilesData.append(FinalSheetName)

for ia in arrayOfFilesData:
    for i1 in ia:
        print(i1)
