import re
from openpyxl import load_workbook
from collections import Counter
import fnmatch


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


f = open('allfreq.txt', 'w', encoding="utf-8")

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

#duplication checker


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


def pythonFile(filetoopen, startreadArea, endReadArea, indextoadd, wordstoignore):
    pyarr = []
    f = open(filetoopen, 'r')
    message = f.readlines()

    # print(message)
    f.close()
    # print(message)
    for myString in message:
        # print(myString)

        try:
            if myString.find(wordstoignore) == -1:
                pyarr.append(myString[myString.index(startreadArea) + indextoadd:myString.index(endReadArea)])
        except:
            pass
    return pyarr


def phoneticcase(filetotopen):
    f = open(filetotopen, 'r')
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
    for i in columarr:
        # print(i)
        # print(userinput)
        if fnmatch.fnmatch(str(i), userinput):
            alllistarr.append(i)
            print(i)
            # print(userinput)
    return alllistarr
    # print(i)


def checkandreturn(matchorsearch, arrayparsein):
    if matchorsearch == 'm':
        return matchcase(arrayparsein)
    else:
        return searchcase(arrayparsein)


# files read form config
arrofileobjects = []

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
        elif x == "py":
            # print("Value check to be deleteed(): " + str(i.split(",")[1].strip()))
            arrofileobjects.append(Files(i.split(",")[1].strip(),
                                         pythonFile(i.split(",")[1].strip(), i.split(",")[2].strip(),
                                                    i.split(",")[3].strip(), int(i.split(",")[4].strip()),
                                                    i.split(",")[5].strip())))
        elif x == "phonetic":
            arrofileobjects.append(Files(i.split(",")[1].strip(), phoneticcase(i.split(",")[1].strip())))

for i in arrofileobjects:
    print(i.getFilename())
    print(i.getArray())

userWeb = ''
userinput = ''
fdup = open('dupefound.txt', 'w', encoding="utf-8")
fnodup = open('nodupefound.txt', 'w', encoding="utf-8")



# for x in range(100):
#     fnodup.writelines("duhhh"+"\n")




for index,abc in enumerate(my_dict):
    wordsfoundaryyyy = []
    print("Scanning: "+str(index)+"/"+str(len(my_dict)))
    sabc=str(abc).lower()

    for c in arrofileobjects:
        # print(c.getFilename())
        if sabc.lower() in (str(name).lower() for name in c.getArray()):
            # print(sabc.lower())

            wordsfoundaryyyy.append(str(c.getFilename()))


    if len(wordsfoundaryyyy)!=0:
        fdup.writelines("Words: " + str(sabc.lower()) + "\n")
        fdup.writelines("File Found In: " + str(wordsfoundaryyyy) + "\n\n")
    else:
        fnodup.writelines("Words: "+str(sabc.lower())+ "\n")
        fnodup.writelines("Frequency: "+str(my_dict[abc])+ "\n\n")












fdup.close()
fnodup.close()
