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

    def getFilename(self, name):
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

def pythonFile(filetoopen):
    pyarr=[]
    f = open(filetoopen,'r')
    message = f.readlines()

    # print(message)
    f.close()
    # print(message)
    for myString in message:
        # print(myString)
        try:
            pyarr.append(myString[myString.index("['")+2:myString.index("']")])
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
        if fnmatch.fnmatch(str(i), userinput):
            alllistarr.append(i)
    return alllistarr
            # print(i)


# files to read
# excelinput('ner.xlsx', 0, 0)
print(pythonFile('senticnet.py'))

userWeb = ''
userinput=''



# while (userWeb != "exit"):
#
#     print("-----------------------------")
#     userWeb = input("Enter 'exit' to exit" + "\n" + "Word duplication check:" + "\n")
#     userinput = str(userWeb)
#
#     if (userinput == "exit"):
#         break
#
#     matchorsearcase = input("Use Match or Search? m=Match, s=Search" + "\n")
#     matchsc = str(matchorsearcase)
#
#     if matchsc == "m":
#         matchcase()
#     elif matchsc == "s":
#         searchcase()
#
#     # searchcase()
#
#     if (len(alllistarr) == 0):
#         print("No match found")
#     else:
#         for i in alllistarr:
#             print(i)
#     print("**Records found: " + str(len(alllistarr)) + "**")
#     alllistarr.clear()
#     print("Total records scanned: " + str(len(columnlist) - 1))
