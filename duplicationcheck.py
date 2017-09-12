from openpyxl import load_workbook

import fnmatch

# print(columnlist)


columnObjectListlist = []


class Files():
    def __init__(self, filename, dataArr):
        self.name = filename
        self.dat = dataArr

    def getArray(self):
        return self.dat

    def getFilename(self):
        return self.name


# regex test
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

    # print(next(data)[0:])

    for r in data:
        # print(r[0])
        columnlist.append(r[columnNo])

    return columnlist

def pythonFile(filetoopen,startreadArea,endReadArea,indextoadd,wordstoignore):
    pyarr=[]
    f = open(filetoopen,'r')
    message = f.readlines()

    # print(message)
    f.close()
    # print(message)
    for myString in message:
        # print(myString)

        try:
            if myString.find(wordstoignore) == -1:
                pyarr.append(myString[myString.index(startreadArea)+indextoadd:myString.index(endReadArea)])
        except:
            pass
    return pyarr


# for i in columnlist:
#     print(i)
def searchcase(columarr):
    alllistarr = []
    for i in columarr:
        # print(i)
        if fnmatch.fnmatch(str(i), "*" + userinput + "*"):
            alllistarr.append(i)
    return alllistarr
            # print(i)


def matchcase(columarr):
    alllistarr = []
    for i in columarr:
        # print(i)
        # print(userinput)
        if fnmatch.fnmatch(str(i), userinput):
            alllistarr.append(i)
            print(i)
            # print(userinput)
    return alllistarr
            # print(i)

def checkandreturn(matchorsearch,arrayparsein):

    if matchorsearch=='m':
        return matchcase(arrayparsein)
    else:
        return searchcase(arrayparsein)


# files to read
# print(excelinput('ner.xlsx', 0, 0))

# print(len(pythonFile('senticnet.py',"['","']",2,"         -------------           ")))
# print(pythonFile('microtext.py','[""','""]',3,"#microtext"))
# print(len(pythonFile('microtext.py','[""','""]',3,"#microtext")))

arrofileobjects=[]

arrofileobjects.append(Files("ner.xlsx",excelinput('ner.xlsx', 0, 0)))
arrofileobjects.append(Files("senticnet.py",pythonFile('senticnet.py',"['","']",2,"         -------------           ")))
arrofileobjects.append(Files("microtext.py",pythonFile('microtext.py','[""','""]',3,"#microtext")))


for i in arrofileobjects:
    print(i.getFilename())
    print(i.getArray())


userWeb = ''
userinput=''



while (userWeb != "exit"):

    print("-----------------------------")
    userWeb = input("Enter 'exit' to exit" + "\n" + "Word duplication check:" + "\n")
    userinput = str(userWeb)

    if (userinput == "exit"):
        break

    matchorsearcase = input("Use Match or Search? m=Match, s=Search" + "\n")
    matchsc = str(matchorsearcase)

    for i in arrofileobjects:
        print("--------")
        print("File:"+str(i.getFilename()))
        print(checkandreturn(matchsc,i.getArray()))
        print("Records Found:"+str(len(checkandreturn(matchsc,i.getArray()))))
        print("Records Scanned:"+str(len(i.getArray())))

