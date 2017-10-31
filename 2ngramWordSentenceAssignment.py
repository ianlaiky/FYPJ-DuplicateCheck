import re
from openpyxl import load_workbook
from collections import Counter
import enchant
import unicodedata


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

    elif str(re.match("^\"([\w\d])+$", str(word))) != "None":
        retuxx = str(word).replace('"', "")

    elif str(re.match("^\'([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace("'", "")

    elif str(re.match("^\"([aA-zZ])+\"$", str(word))) != "None":
        retuxx = str(word).replace('"', "")

    elif str(re.match("^\"([aA-zZ])+\'[sS]\"$", str(word))) != "None":
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

    elif str(re.match("^\![\w\d]+$", str(word))) != "None":
        retuxx = str(word).replace("!", "")

    elif str(re.match("^([aA-zZ])+(\.\")$", str(word))) != "None":
        retuxx = str(word).replace('."', "")

    elif str(re.match("^([aA-zZ])+\($", str(word))) != "None":
        retuxx = str(word).replace('(', "")

    elif str(re.match("^\'\'[\w\d]+$", str(word))) != "None":
        retuxx = str(word).replace("'", "")

    elif str(re.match("^\'\'[\w]+\-[\w]+$", str(word))) != "None":
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
    elif str(re.match("^\“([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('“', "")

    elif str(re.match("^\“([aA-zZ])+\”$", str(word))) != "None":
        retuxx = str(word).replace('“', "")
        retuxx = str(retuxx).replace('”', "")

    elif str(re.match("^([aA-zZ])+\.\”$", str(word))) != "None":
        retuxx = str(word).replace('.”', "")

    elif str(re.match("^\[([\w])+$", str(word))) != "None":
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

    elif str(re.match("^\‘+([aA-zZ])+\’+$", str(word))) != "None":
        retuxx = str(word).replace('‘', "")
        retuxx = str(retuxx).replace('’', "")

    elif str(re.match("^\‘+([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('‘', "")
    elif str(re.match("^([aA-zZ])+\‘+$", str(word))) != "None":
        retuxx = str(word).replace('‘', "")
    elif str(re.match("^\/([\w\d])+$", str(word))) != "None":
        retuxx = str(word).replace('/', "")
    elif str(re.match("^([\w\d])+\/$", str(word))) != "None":
        retuxx = str(word).replace('/', "")
    elif str(re.match("^\/([\w\d])+\/$", str(word))) != "None":
        retuxx = str(word).replace('/', "")
    elif str(re.match("^([$]+)$", str(word))) != "None":
        retuxx = str(word).replace('$', "")
    elif str(re.match("^\"([\w\'])+$", str(word))) != "None":
        retuxx = str(word).replace('"', "")
    elif str(re.match("^\(([\w\.\-])+$", str(word))) != "None":
        retuxx = str(word).replace('(', "")
    elif str(re.match("^\"([\w]+\'[\w]+)$", str(word))) != "None":
        retuxx = str(word).replace('"', "")
    elif str(re.match("^\'([\w]+\'[\w]+)$", str(word))) != "None":
        retuxx = str(word).replace("'", "")
    elif str(re.match("^\(([\w]+\'[\w]+)$", str(word))) != "None":
        retuxx = str(word).replace("(", "")

    elif str(re.match("^([\w]+\'[\w]+)\;$", str(word))) != "None":
        retuxx = str(word).replace(";", "")

    elif str(re.match("^([\w]+\-[\w]+)\;$", str(word))) != "None":
        retuxx = str(word).replace(";", "")

    elif str(re.match("^([\w\d])+\]$", str(word))) != "None":
        retuxx = str(word).replace("]", "")
    elif str(re.match("^\[([\w\d])+$", str(word))) != "None":
        retuxx = str(word).replace("[", "")
    elif str(re.match("^[b]\]([\w\d])+$", str(word))) != "None":
        retuxx = str(word).replace("b]", "")
    elif str(re.match("^\[[b]\]([\w\d])+$", str(word))) != "None":
        retuxx = str(word).replace("[b]", "")

    elif str(re.match("^([\w])+\"\;$", str(word))) != "None":
        retuxx = str(word).replace('";', "")

    elif str(re.match("^\"\$([\w])+$", str(word))) != "None":
        retuxx = str(word).replace('"$', "")

    elif str(re.match("^([\w])+\.\"\;$", str(word))) != "None":
        retuxx = str(word).replace('.";', "")

    elif str(re.match("^([\w])+\)\?\"$", str(word))) != "None":
        retuxx = str(word).replace(')?"', "")

    elif str(re.match("^([aA-zZ])+\/[sS]$", str(word))) != "None":
        retuxx = str(word).replace('/s', "")
        retuxx = str(retuxx).replace('/S', "")

    elif str(re.match("^\>([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('>', "")
    elif str(re.match("^\'([aA-zZ])+\'\?$", str(word))) != "None":
        retuxx = str(word).replace("'", "")
        retuxx = str(retuxx).replace("?", "")

    elif str(re.match("^\"([aA-zZ])+\.\"$", str(word))) != "None":
        retuxx = str(word).replace('"', "")
        retuxx = str(retuxx).replace(".", "")

    elif str(re.match("^([aA-zZ])+\-$", str(word))) != "None":
        retuxx = str(word).replace('-', "")

    elif str(re.match("^([aA-zZ])+\:\-$", str(word))) != "None":
        retuxx = str(word).replace(':-', "")

    elif str(re.match("^([aA-zZ])+\(\?$", str(word))) != "None":
        retuxx = str(word).replace('(?', "")

    elif str(re.match("^\*([aA-zZ])+\*$", str(word))) != "None":
        retuxx = str(word).replace('*', "")

    elif str(re.match("^([aA-zZ])+\.\[\/[i][m][g]\]$", str(word))) != "None":
        retuxx = str(word).replace('.[/img]', "")
    elif str(re.match("^([aA-zZ])+\[\/[i][m][g]\]$", str(word))) != "None":
        retuxx = str(word).replace('[/img]', "")

    elif str(re.match("^\!([aA-zZ])+$", str(word))) != "None":
        retuxx = str(word).replace('!', "")

    elif str(re.match("^([aA-zZ])+\.\’$", str(word))) != "None":
        retuxx = str(word).replace(".’", "")


    elif str(re.match("^([\w])+\"$", str(word))) != "None":
        retuxx = str(word).replace('"', "")

    else:
        retuxx = word

    return str(retuxx).strip()


def wordduplicationcheckatEnd(wordstocheck):
    if wordstocheck[-1:] == ".":
        if wordstocheck[-2:-1] != ".":
            return (specificcharacterremoverandother((wordstocheck)[0:-1]))
        else:
            return (specificcharacterremoverandother((wordstocheck)))
    elif wordstocheck[-2:] == "'s":
        return (specificcharacterremoverandother(wordstocheck[0:-2]))
    elif wordstocheck[-2:] == "’s":
        return (specificcharacterremoverandother(wordstocheck[0:-2]))
    else:
        return (specificcharacterremoverandother((wordstocheck)))


counttttt = 0


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


forumdataforreading = "../datafiles/sgforums.xlsx"

arrayoffilteredsentences = []
listofunformattedsentence = []

for i in excelinput(forumdataforreading, 0, 0):
    # print(i)
    print("Currently scanning Line: " + str(counttttt))
    counttttt = counttttt + 1
    listofunformattedsentence.append(i)
    i = str(i).replace('\n', " ")
    i = str(i).replace('\\n', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")
    i = str(i).replace('', " ")

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

    # print(ixre)
    # input()

    if str(ixre).find(" ") != -1:

        tempsetecehold = ""

        sentencestringfiltered = []
        for x321 in re.split(" |,", ixre):
            tempword = wordduplicationcheckatEnd(specificcharacterremoverandother(str(x321).strip())).strip()
            if tempword != "":
                if tempword != " ":
                    tempsetecehold = tempsetecehold + " " + tempword
        arrayoffilteredsentences.append(str(tempsetecehold).lower())



        # print(arrayoffilteredsentences)

    else:
        # sentencestringfiltered = []
        # sentencestringfiltered.append(str(ixre).strip().strip())
        arrayoffilteredsentences.append(str(ixre).lower())

listofwordstocheck = []

textreader = open("nGramCandidates.txt", 'r', encoding="utf-8")
wordsfromfile = textreader.readlines()

inputsen = open("NGramsentencesAssignment.txt", 'w', encoding="utf-8")

for readme in wordsfromfile:
    print(str(readme))
    listofwordstocheck.append(str(readme).strip())

for index1, op in enumerate(listofwordstocheck):
    for index, opch in enumerate(arrayoffilteredsentences):
        # if str(op).lower() in (str(checkword).lower() for checkword in opch):
        if str(op).lower() in (str(opch).split(" ")):
            # if str(opch).find(str(op.lower()))!= -1:
            inputsen.writelines(str(op) + " | " + str(listofunformattedsentence[index]) + "\n\n")
            # else:
            #     print("Error: Word is: "+str(op))
    print("Current: " + str(index1) + " " + str(len(listofwordstocheck)) + "  " + str(
        (round((int(index1) / int(len(listofwordstocheck))) * 100, 2))) + " %")

textreader.close()
inputsen.close()
