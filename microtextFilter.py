import re
from openpyxl import load_workbook
from collections import Counter
import enchant
import unicodedata

# forum data for reading
forumdataforreading = "datafiles\sgforums.xlsx"


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


# comparing 2 words: https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison-in-python
def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())


def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)


tempppppaarrrrr = []


# punctuation remover
def multiplepunctuationRemover(words):
    line = re.sub('\.\.+', ' ', words)
    line = re.sub('\!!+', ' ', line)
    line = re.sub('\?\?+', ' ', line)
    line = re.sub('\-\-+', ' ', line)
    line = re.sub('\_\_+', ' ', line)
    line = re.sub('\=\=+', ' ', line)

    # if str(re.match("^[aA-zZ]+\/[aA-zZ]+$", str(line))) != "None":
    #     line=line.replace("/"," ")

    return line


def specificcharacterremoverandother(word):
    if str(re.match("^\([\w\d]+$", str(word))) != "None":
        retuxx = str(word).replace("(", "")
    elif str(re.match("^([\w\d])+(\))$", str(word))) != "None":
        retuxx = str(word).replace(")", "")
    elif str(re.match("^\"([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('"', "")
    elif str(re.match("^\'([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace("'", "")
    elif str(re.match("^\"([aA-zZ])+\"$", str(word))) != "None":
        retuxx = str(word).replace('"', "")
    elif str(re.match("^\'([aA-zZ])+\'$", str(word))) != "None":
        retuxx = str(word).replace("'", "")
    elif str(re.match("^([aA-zZ])+\'$", str(word))) != "None":
        retuxx = str(word).replace("'", "")
    elif str(re.match("^([aA-zZ\-])+\"$", str(word))) != "None":
        retuxx = str(word).replace('"', "")
    elif str(re.match("^\([aA-zZ]+\)$", str(word))) != "None":
        retuxx = str(word).replace("(", "")
        retuxx = str(retuxx).replace(")", "")
    elif str(re.match("^[aA-zZ]+\.;$", str(word))) != "None":
        retuxx = str(word).replace(".;", "")
    elif str(re.match("^[\w\d]+(\?+)$", str(word))) != "None":
        retuxx = str(word).replace("?", "")
    elif str(re.match("^[\w\d]+(:+)$", str(word))) != "None":
        retuxx = str(word).replace(":", "")
    elif str(re.match("^[\w\d]+(;+)$", str(word))) != "None":
        retuxx = str(word).replace(";", "")
    elif str(re.match("^[\w\d]+(!+)$", str(word))) != "None":
        retuxx = str(word).replace("!", "")
    elif str(re.match("^([aA-zZ])+(\.\")$", str(word))) != "None":
        retuxx = str(word).replace('."', "")
    elif str(re.match("^([aA-zZ])+\($", str(word))) != "None":
        retuxx = str(word).replace('(', "")
    elif str(re.match("^\'\'[\w\d]+$", str(word))) != "None":
        retuxx = str(word).replace("'", "")
    elif str(re.match("^\'[\d]+\'$", str(word))) != "None":
        retuxx = str(word).replace("'", "")
    elif str(re.match("^([aA-zZ])+\.\'\'$", str(word))) != "None":
        retuxx = str(word).replace(".''", "")
    elif str(re.match("^“([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace("“", "")
    elif str(re.match("^([\w\d])+\"\/\>$", str(word))) != "None":
        retuxx = str(word).replace('"/>', "")
    elif str(re.match("^([aA-zZ])+\)!$", str(word))) != "None":
        retuxx = str(word).replace(")!", "")
    elif str(re.match("^([aA-zZ])+\.\'$", str(word))) != "None":
        retuxx = str(word).replace(".'", "")
    elif str(re.match("^([aA-zZ])+\'\'$", str(word))) != "None":
        retuxx = str(word).replace("''", "")
    elif str(re.match("^\'\'([aA-zZ])+\'\'$", str(word))) != "None":
        retuxx = str(word).replace("'", "")
    elif str(re.match("^([aA-zZ])+\([sS]\)$", str(word))) != "None":
        retuxx = str(word).replace("(s)", "")
        retuxx = str(retuxx).replace("(S)", "")
    elif str(re.match("^\"([aA-zZ])+\'\'$", str(word))) != "None":
        retuxx = str(word).replace("'", "")
        retuxx = str(retuxx).replace('"', "")
    elif str(re.match("^([aA-zZ])+\?\;$", str(word))) != "None":
        retuxx = str(word).replace("?;", "")
    elif str(re.match("^([aA-zZ])+\"\?$", str(word))) != "None":
        retuxx = str(word).replace('"?', "")
    elif str(re.match("^\.([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('.', "")
    elif str(re.match("^([aA-zZ])+\*$", str(word))) != "None":
        retuxx = str(word).replace('*', "")
    elif str(re.match("^\'\'([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace("''", "")
    elif str(re.match("^\?([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace("?", "")
    elif str(re.match("^([aA-zZ])+!\)$", str(word))) != "None":
        retuxx = str(word).replace("!)", "")
    elif str(re.match("^([aA-zZ])+\?\)$", str(word))) != "None":
        retuxx = str(word).replace("?)", "")
    elif str(re.match("^([aA-zZ])+\}$", str(word))) != "None":
        retuxx = str(word).replace("}", "")
    elif str(re.match("^\'([aA-zZ\-])+\'$", str(word))) != "None":
        retuxx = str(word).replace("'", "")
    elif str(re.match("^\"([aA-zZ\-])+\"$", str(word))) != "None":
        retuxx = str(word).replace('"', "")
    elif str(re.match("^([aA-zZ\-])+\?\"$", str(word))) != "None":
        retuxx = str(word).replace('?"', "")
    elif str(re.match("^([aA-zZ\-])+\"\?$", str(word))) != "None":
        retuxx = str(word).replace('"?', "")
    elif str(re.match("^\"([aA-zZ\-])+\'\"$", str(word))) != "None":
        retuxx = str(word).replace('"', "")
        retuxx = str(retuxx).replace("'", "")
    elif str(re.match("^([aA-zZ\-])+\.\)$", str(word))) != "None":
        retuxx = str(word).replace('.)', "")
    elif str(re.match("^([aA-zZ\-])+\)$", str(word))) != "None":
        retuxx = str(word).replace(')', "")
    elif str(re.match("^([aA-zZ])+\.\'$", str(word))) != "None":
        retuxx = str(word).replace(".'", "")
    elif str(re.match("^\[([aA-zZ/])+\]$", str(word))) != "None":
        retuxx = str(word).replace("[", "")
        retuxx = str(retuxx).replace("]", "")
    elif str(re.match("^\[([aA-zZ/])+$", str(word))) != "None":
        retuxx = str(word).replace("[", "")
    elif str(re.match("^\(([aA-zZ])+\):$", str(word))) != "None":
        retuxx = str(word).replace("(", "")
        retuxx = str(retuxx).replace("):", "")
    elif str(re.match("^\"\(([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('"(', "")
    elif str(re.match("^([aA-zZ])+\)\:$", str(word))) != "None":
        retuxx = str(word).replace('):', "")
    elif str(re.match("^\[([\w\d])+\]$", str(word))) != "None":
        retuxx = str(word).replace("[", "")
        retuxx = str(retuxx).replace("]", "")
    elif str(re.match("^([aA-zZ])+\’$", str(word))) != "None":
        retuxx = str(word).replace('’', "")
    elif str(re.match("^([aA-zZ])+\”$", str(word))) != "None":
        retuxx = str(word).replace('”', "")
    elif str(re.match("^\”([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('”', "")
    elif str(re.match("^([aA-zZ])+\.\”$", str(word))) != "None":
        retuxx = str(word).replace('.”', "")
    elif str(re.match("^\[([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('[', "")
    elif str(re.match("^([aA-zZ])+\”$", str(word))) != "None":
        retuxx = str(word).replace('”', "")
    elif str(re.match("^([aA-zZ])+\!\?$", str(word))) != "None":
        retuxx = str(word).replace('!?', "")
    elif str(re.match("^([aA-zZ])+\?\!$", str(word))) != "None":
        retuxx = str(word).replace('?!', "")
    elif str(re.match("^([aA-zZ])+\?\'$", str(word))) != "None":
        retuxx = str(word).replace("?'", "")
    elif str(re.match("^\"([aA-zZ])+\?$", str(word))) != "None":
        retuxx = str(word).replace('"', "")
        retuxx = str(retuxx).replace('?', "")
    elif str(re.match("^([aA-zZ])+\!\"$", str(word))) != "None":
        retuxx = str(word).replace('!"', "")
    elif str(re.match("^\-([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('-', "")
    elif str(re.match("^\`+([aA-zZ])+\`+$", str(word))) != "None":
        retuxx = str(word).replace('`', "")
    elif str(re.match("^\`+([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('`', "")
    elif str(re.match("^([aA-zZ])+\`+$", str(word))) != "None":
        retuxx = str(word).replace('`', "")
    elif str(re.match("^\‘+([aA-zZ])+\‘+$", str(word))) != "None":
        retuxx = str(word).replace('‘', "")
    elif str(re.match("^\‘+([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('‘', "")
    elif str(re.match("^([aA-zZ])+\‘+$", str(word))) != "None":
        retuxx = str(word).replace('‘', "")
    elif str(re.match("^\/([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('/', "")
    elif str(re.match("^([aA-zZ])+\/$", str(word))) != "None":
        retuxx = str(word).replace('/', "")
    elif str(re.match("^\/([aA-zZ])+\/$", str(word))) != "None":
        retuxx = str(word).replace('/', "")
    elif str(re.match("^([$]+)$", str(word))) != "None":
        retuxx = str(word).replace('$', "")
    elif str(re.match("^\"([\w\'])+$", str(word))) != "None":
        retuxx = str(word).replace('"', "")
    elif str(re.match("^\(([\w\.])+$", str(word))) != "None":
        retuxx = str(word).replace('(', "")
    elif str(re.match("^\"([\w]+\'[\w]+)$", str(word))) != "None":
        retuxx = str(word).replace('"', "")
    else:
        retuxx = word
    return str(retuxx).strip()


def wordduplicationcheckatEnd(wordstocheck):
    if wordstocheck[-1:] == ".":
        if wordstocheck[-2:-1] != ".":
            tempppppaarrrrr.append(specificcharacterremoverandother((wordstocheck)[0:-1]))
        else:
            tempppppaarrrrr.append(specificcharacterremoverandother((wordstocheck)))
    elif wordstocheck[-2:] == "'s":
        tempppppaarrrrr.append(specificcharacterremoverandother(wordstocheck[0:-2]))
    elif wordstocheck[-2:] == "’s":
        tempppppaarrrrr.append(specificcharacterremoverandother(wordstocheck[0:-2]))
    else:
        tempppppaarrrrr.append(specificcharacterremoverandother((wordstocheck)))


counttttt = 0

# RAW DATA HERE
for i in excelinput(forumdataforreading, 0, 0):
    # print(i)
    print("Currently scanning Line: " + str(counttttt))
    counttttt = counttttt + 1
    i = str(i).replace('\n', " ")
    i = str(i).replace('\\n', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('…', '...')

    # i = str(i).replace('/', " / ")
    # i = str(i).replace('"', " ")
    # i = str(i).replace('(', " ")
    # i = str(i).replace(')', " ")
    # i = str(i).replace('“', " ")
    # i = str(i).replace('. ', " ")
    # i = str(i).replace(';', " ")
    # i = str(i).replace('[', " ")
    # i = str(i).replace(']', " ")
    # i = str(i).lower()
    # do blank check to see if have space

    ixre = multiplepunctuationRemover(str(i))

    # .replace to fix Ellipsis problem
    if str(ixre).find(" ") != -1:
        for x321 in re.split(" |,", ixre):
            wordduplicationcheckatEnd(str(x321).strip())
    else:

        wordduplicationcheckatEnd(str(ixre).strip())
print("Converting to lowercase...")
newtempppppaarrrrr = []
for ghty in tempppppaarrrrr:
    newtempppppaarrrrr.append(str(ghty).lower())

my_dict = Counter(newtempppppaarrrrr)

del my_dict[' ']
del my_dict['']

# total freq
f = open('allfreq.txt', 'w', encoding="utf-8")
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
            for re in i.strip().split("'"):
                if re.find("[") == -1:
                    if re.find("]") == -1:
                        if re != " ":
                            if re != "":
                                # if x not in phoneticarr:
                                # print(re)
                                phoneticarr.append(re)

    # for index,x1 in enumerate(phoneticarr):
    #     print(index)
    #     print(len(phoneticarr))
    #     if x1 not in newphonecticlist:
    #         newphonecticlist.append(x1)
    #
    # return newphonecticlist
    newphonecticlist = list(set(phoneticarr))
    # print(phoneticarr)
    return newphonecticlist


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
                                                    i.split(",")[3].strip(), int(len(i.split(",")[3].strip())),
                                                    i.split(",")[4].strip())))
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
    my_dicInArray.append(specificcharacterremoverandother(sabc))

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


# filtering only non-duplication, thus saving to another file; also checks for numbers string only
# single items to remove
def characterinvalidationchecker(word):
    texttochecktoinvalidate = ['...', '?', '-', '?', '!', '=', '--', "'", '/b', '>', '/', '+', '–', '<!---', '/>',
                               '---', ')', '(', '[/b]', '', '', '', '%', '[/quote]', '--->', '"', '$', '|', '—', '”',
                               '·',
                               "''", ';', "\\", '>>', '$$$', '===', '[', ']', '___', '->', ':', '@', '<!',
                               '<w:lsdexception', 'locked="false"', 'unhidewhenused="false"', 'name="medium', '£',
                               '€ڰ:', '_', '#', '?"', '<', '~', "'')", '?;','=>',':-']
    returnvalue = True

    for io in texttochecktoinvalidate:
        # print(len(texttochecktoinvalidate))
        # print("I: " + word)
        # print("C: " + io)
        if str(io) == str(word):
            # print(word)
            # print("true")
            returnvalue = False
    if str(re.match("^[0-9]+\)$", word)) != "None":
        returnvalue = False

    elif str(re.match("^[0-9]+$", word)) != "None":
        returnvalue = False
    elif str(re.match("^\([0-9]+\)$", word)) != "None":
        returnvalue = False
    elif str(re.match("^\([0-9]+$", word)) != "None":
        returnvalue = False
    elif str(re.match("^[0-9]+%$", word)) != "None":
        returnvalue = False
    elif str(re.match("^\$[0-9]+$", word)) != "None":
        returnvalue = False
    elif str(re.match("^[^(\w\d)]$", word)) != "None":
        returnvalue = False

    return returnvalue


dictus = enchant.Dict("en_US")
dictgb = enchant.Dict("en_GB")

print("Removing english words...")
listofdicttoremoveforvariant = []
for uixxx in parseinDictDiff:
    listofdicttoremoveforvariant.append(uixxx)

verynewtempppppaarrrrr = list(set(tempppppaarrrrr).difference(set(listofdicttoremoveforvariant)))
uniqueverynewtempppppaarrrrr = [item.lower() for item in verynewtempppppaarrrrr]

indexforengremoval = 0

# sort special char to diff file, save all non-dup to one file
for ixxx in sorted(parseinDictDiff, key=parseinDictDiff.get, reverse=True):
    # ixxx = str(specificcharacterremoverandother(ixxxo))
    if dictus.check(ixxx) is False:
        if dictgb.check(ixxx) is False:
            tempwordthatl = ""

            try:
                tempwordthatl = str(tempwordthatl) + " / " + str(
                    verynewtempppppaarrrrr[uniqueverynewtempppppaarrrrr.index(ixxx.lower())])
            except:
                print("not: " + str(ixxx))
                pass

            line = re.search('[^A-Za-z]', str(ixxx))
            # print(line)
            if 'None' != str(line):
                if characterinvalidationchecker(str(ixxx).strip()) is True:
                    # (variant assignment) start word check upper and lower case and end to variants list (*performance issue)

                    # for checkkwor in tempppppaarrrrr:
                    #     if caseless_equal(str(checkkwor), str(ixxx)) is True:
                    #         tempwordsthatonlyrunperword = str(tempwordsthatonlyrunperword) + " / " + str(checkkwor)
                    # end upper lower check

                    # new test

                    fnodupwspecial.writelines("Word: " + str(ixxx) + " " + str(tempwordthatl) + "\n")
                    fnodupwspecial.writelines("Frequency: " + str(my_dict[ixxx]) + "\n\n")

            # for chhs in tempppppaarrrrr:
            #     if caseless_equal(str(chhs),str(ixxx)) is True:
            #         tempwordthatl=str(tempwordthatl)+" / "+str(chhs)

            # new test


            if characterinvalidationchecker(str(ixxx).strip()) is True:
                fnodup.writelines("Word: " + str(ixxx) + " " + str(tempwordthatl) + "\n")
                fnodup.writelines("Frequency: " + str(my_dict[ixxx]) + "\n\n")
    print("English removal & variant assignment: " + str(indexforengremoval) + "/" + str(
        len(parseinDictDiff)) + "  " + str(round((int(indexforengremoval) / int(len(parseinDictDiff))) * 100)) + "%")
    indexforengremoval = indexforengremoval + 1

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
