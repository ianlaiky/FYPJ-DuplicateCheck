import re
from openpyxl import load_workbook
from collections import Counter
import fnmatch
import operator


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


# class DataValue():
#     def __init__(self, itemm, countt):
#         self.item = itemm
#         self.count = countt
#
#     def getitem(self):
#         return self.item
#
#     def getitemCount(self):
#         return self.countt
#
#     def setitemCounr(self, itemm):
#         self.item = itemm
#         return self.item


tempppppaarrrrr = []


# punctuation remover
def multiplepunctuationRemover(words):
    line = re.sub('\.\.+', '...', words)
    line = re.sub('\!!+', '!', line)
    line = re.sub('\?\?+', '?', line)
    line = re.sub('\-\-+', '---', line)
    line = re.sub('\_\_+', '___', line)
    line = re.sub('\=\=+', '===', line)

    return line


def wordduplicationcheck(wordstocheck):
    if wordstocheck[-1:] == ".":
        if wordstocheck[-2:-1] != ".":

            # if multiplepunctuationRemover(wordstocheck[0:-1])[-1:] == "?":
            #
            #     if multiplepunctuationRemover(wordstocheck[0:-1])[-2:-1] != "?":
            #         tempppppaarrrrr.append(
            #             multiplepunctuationRemover(multiplepunctuationRemover(wordstocheck[0:-1]))[0:-1])
            #
            #     else:
            #         tempppppaarrrrr.append(multiplepunctuationRemover(wordstocheck))
            # else:

            tempppppaarrrrr.append((wordstocheck)[0:-1])

        else:
            tempppppaarrrrr.append((wordstocheck))

    elif wordstocheck[-1:] == ":":

        tempppppaarrrrr.append((wordstocheck[0:-1]))

    elif wordstocheck[-1:] == "?":

        tempppppaarrrrr.append((wordstocheck[0:-1]))

    else:

        tempppppaarrrrr.append((wordstocheck))


f = open('allfreq.txt', 'w', encoding="utf-8")

counttttt = 0

# RAW DATA HERE
for i in excelinput("datafiles\sgforums.xlsx", 0, 0):
    # print(i)
    print("Currently scanning Line: " + str(counttttt))
    counttttt = counttttt + 1
    i = str(i).replace('\n', " ")
    i = str(i).replace('\\n', " ")
    i = str(i).replace('"', " ")
    # i = str(i).replace('(', " ")
    # i = str(i).replace(')', " ")
    i = str(i).replace('“', " ")
    # i = str(i).replace(';', " ")
    # i = str(i).replace('[', " ")
    # i = str(i).replace(']', " ")
    i = str(i).lower()
    # do blank check to see if have space


    # .replace to fix Ellipsis problem
    if str(i).find(" ") != -1:
        for x in re.split(" |,", i):
            # print(x)
            # f.writelines(x+"\n")
            wordduplicationcheck(multiplepunctuationRemover(str(x).strip().replace('…', '...')))
    else:
        wordduplicationcheck(multiplepunctuationRemover(str(i).strip().replace('…', '...')))

my_dict = Counter(tempppppaarrrrr)

del my_dict[' ']
del my_dict['']

for fg in sorted(my_dict, key=my_dict.get, reverse=True):
    f.writelines(str(fg) + "\t\t" + str(my_dict[fg]) + "\n")
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
    f = open(filetoopen, 'r', encoding="utf8")
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
        elif x == "text":
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
fnodupwspecial = open('nodupefoundSpecialCharacter.txt', 'w', encoding="utf-8")

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

    # found
    listyincheck = list(set(c.getArray()).intersection(set(my_dicInArray)))
    for gh in listyincheck:
        if gh in parseinDict:
            parseinDict[gh] = str(parseinDict[gh]) + ", " + str(c.getFilename())
        else:
            parseinDict[gh] = str("Word found in: ") + str(c.getFilename())

listwhosewordsarenotfound = []
temparrtocheckagainstdata = []
print("Saving File.....")
for gitdata in parseinDict:
    temparrtocheckagainstdata.append(gitdata)

oldlistwhosewordsarenotfound = list(set(my_dicInArray).difference(set(temparrtocheckagainstdata)))
listwhosewordsarenotfound = []
# not found

# filtering globally
print("Cleaning up links...")
for links in oldlistwhosewordsarenotfound:
    if 'http' in links:
        print(links)
    if 'https' in links:
        print(links)
    if 'www.' in links:
        print(links)
    if '.com' in links:
        print(links)

    if 'http' not in links:
        if 'https' not in links:
            if 'www.' not in links:
                if '.com' not in links:
                    listwhosewordsarenotfound.append(links)
# not found in db
for savedata in listwhosewordsarenotfound:
    parseinDictDiff[savedata] = my_dict[savedata]


# filtering only non-duplication, thus saving to another file
def characterinvalidationchecker(word):
    texttochecktoinvalidate = ['...', '?', '-', '?', '!', '=', '--', "'", '/b', '>', '/', '+', '–', '<!---', '/>']
    returnvalue = True

    for io in texttochecktoinvalidate:
        # print(len(texttochecktoinvalidate))
        # print("I: " + word)
        # print("C: " + io)
        if str(io) == str(word):
            # print(word)
            # print("true")
            returnvalue = False
    return returnvalue


# sort special char to diff file, save all non-dup to one file
for ixxx in sorted(parseinDictDiff, key=parseinDictDiff.get, reverse=True):
    line = re.search('[^A-Za-z]', str(ixxx))
    # print(line)
    if 'None' != str(line):
        if characterinvalidationchecker(str(ixxx).strip()) is True:
            fnodupwspecial.writelines("Word: " + str(ixxx) + "\n")
            fnodupwspecial.writelines("Frequency: " + str(my_dict[ixxx]) + "\n\n")

    fnodup.writelines("Word: " + str(ixxx) + "\n")
    fnodup.writelines("Frequency: " + str(my_dict[ixxx]) + "\n\n")

my_dict2fordup = {}

for i in parseinDict:
    my_dict2fordup[i] = my_dict[i]

# found
for oiw in sorted(my_dict2fordup, key=my_dict2fordup.get, reverse=True):
    # fdup.writelines("Word: " + str(oiw) + " | Freq: " + str(my_dict[oiw]) + "\n")
    fdup.writelines("Word: " + str(oiw) + " | Freq: " + str(my_dict2fordup[oiw]) + "\n")

    fdup.writelines("File : " + str(parseinDict[oiw]) + "\n\n")

print(len(listwhosewordsarenotfound))
print("All complete")

fdup.close()
fnodup.close()
fnodupwspecial.close()
