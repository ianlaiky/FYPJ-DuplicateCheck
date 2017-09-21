from openpyxl import load_workbook

import fnmatch

# print(columnlist)


columnObjectListlist = []
arrofileobjects = []

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


def pythonFile(filetoopen, startreadArea, endReadArea, indextoadd, wordstoignore):
    pyarr = []
    f = open(filetoopen, 'r', encoding="utf8")
    message = f.readlines()

    # print(message)
    f.close()
    # print(message)
    for myString in message:
        # print(myString)

        try:
            if myString.find(wordstoignore) == -1:
                if startreadArea!="":
                    pyarr.append(myString[myString.index(startreadArea) + indextoadd:myString.index(endReadArea)])
                else:
                    pyarr.append(myString.replace("\n",""))
        except:
            pass
    return pyarr


def phoneticcase(filetotopen):
    f = open(filetotopen, 'r', encoding="utf8")
    message = f.readlines()

    f.close()
    phoneticarr = []
    newphonecticlist = []

    for m in message:

        for i in m.strip().split(","):
            # print(i)
            for x in i.strip().split("'"):
                if x.find("[") == -1:
                    if x.find("]") == -1:
                        if x != " ":
                            if x != "":
                                # print(x)
                                phoneticarr.append(x)

    for x in phoneticarr:
        if x not in newphonecticlist:
            newphonecticlist.append(x)

    return newphonecticlist

    print(newphonecticlist)


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
    # for i in columarr:
        # print(i)
        # print(userinput)
        # if fnmatch.fnmatch(str(i), userinput):
        #     alllistarr.append(i)
            # print(i)
            # print(userinput)
    if userinput in columarr:
        alllistarr.append(userinput)

    return alllistarr
    # print(i)


def checkandreturn(matchorsearch, arrayparsein):
    if matchorsearch == 'm':
        return matchcase(arrayparsein)
    else:
        return searchcase(arrayparsein)


# files read form config


confff = open("config.txt", 'r')
conf = confff.readlines()
confff.close()

for i in conf:
    if i[:1] != "#":
        x = i.split(",")[0].strip()
        print(x)
        if x == "xlsx":
            # print("Value check to be deleteed(): "+str(i.split(",")[1].strip())+str(i.split(",")[2].strip())+str(i.split(",")[3].strip()))
            arrofileobjects.append(Files(i.split(",")[1].strip(),
                                         excelinput(i.split(",")[1].strip(), int(i.split(",")[2].strip()),
                                                    int(i.split(",")[3].strip()))))
        elif x == "text":
            # print("Value check to be deleteed(): " + str(i.split(",")[1].strip()))
            arrofileobjects.append(Files(i.split(",")[1].strip(),
                                         pythonFile(i.split(",")[1].strip(), i.split(",")[2].strip(),
                                                    i.split(",")[3].strip(), int(len(i.split(",")[3].strip())),
                                                    i.split(",")[4].strip())))
        elif x == "phonetic":
            arrofileobjects.append(Files(i.split(",")[1].strip(), phoneticcase(i.split(",")[1].strip())))


print("Files"+str(len(arrofileobjects)))
for iiiii in arrofileobjects:
    print("Files loaded")
    print(iiiii.getFilename())

# for xxxx in arrofileobjects:
#     print(xxxx.getArray())
# print(arrofileobjects[1].getArray())

userWeb = ''
userinput = ''

while (userWeb != "exit()"):

    print("-----------------------------")
    userWeb = input("Enter 'exit()' to exit" + "\n" + "Word duplication check:" + "\n")
    userinput = str(userWeb)

    if (userinput == "exit()"):
        break

    matchorsearcase = input("Use Match or Search? m=Match, s=Search" + "\n")
    matchsc = str(matchorsearcase)
    filenames=[]
    for i in arrofileobjects:
        print("--------")
        print("File:" + str(i.getFilename()))
        print(checkandreturn(matchsc, i.getArray()))
        print("Records Found:" + str(len(checkandreturn(matchsc, i.getArray()))))
        print("Records Scanned:" + str(len(i.getArray())))

        if len(checkandreturn(matchsc, i.getArray()))>0:
            filenames.append(i.getFilename())

    print("---***************-----")
    print("Word: "+str(userinput)+" is found in: ")

    print(filenames)

