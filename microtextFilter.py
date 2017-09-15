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

# RAW DATA HERE
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

# duplication checker


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
                if startreadArea != "":
                    pyarr.append(myString[myString.index(startreadArea) + indextoadd:myString.index(endReadArea)])
                else:
                    pyarr.append(myString.replace("\n", ""))
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
    print("Files loaded")
    print(i.getFilename())
    print(i.getArray())

userWeb = ''
userinput = ''
fdup = open('dupefound.txt', 'w', encoding="utf-8")
fnodup = open('nodupefound.txt', 'w', encoding="utf-8")

# for x in range(100):
#     fnodup.writelines("duhhh"+"\n")

my_dicInArray = []

parseinDict = {}
parseinDictDiff = {}

for index, abc in enumerate(my_dict):
    wordsfoundaryyyy = []
    print("Scanning: " + str(index) + "/" + str(len(my_dict)) + "\t" + str(
        round(int(index) / int(len(my_dict)) * 100, 2)) + "% Completed")
    sabc = str(abc).lower()
    my_dicInArray.append(sabc)

for c in arrofileobjects:
    print("Processing File: " + str(c.getFilename()))
    listyincheck = []

    listyincheck = list(set(c.getArray()).intersection(set(my_dicInArray)))
    for gh in listyincheck:
        if gh in parseinDict:
            parseinDict[gh] = str(parseinDict[gh]) + ", " + str(c.getFilename())
        else:
            parseinDict[gh] = str("Word found in: ") + str(c.getFilename())
    listyincheckdiff = list(set(my_dicInArray).difference(set(c.getArray())))
    # print(listyincheckdiff)

    for wer in listyincheckdiff:
        parseinDictDiff[wer] = my_dict[wer]

for ixxx in parseinDictDiff:
    fnodup.writelines("Word: " + str(ixxx) + "\n")
    fnodup.writelines("Frequency: " + str(my_dict[ixxx]) + "\n\n")

for oiw in parseinDict:
    fdup.writelines("Word: " + str(oiw) +" | Freq: "+ str(my_dict[oiw])+"\n")
    fdup.writelines("File : " + str(parseinDict[oiw]) + "\n\n")

print("All complete")

fdup.close()
fnodup.close()