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
    elif str(re.match("^([\w\d])+\]$", str(word))) != "None":
        retuxx = str(word).replace("]", "")
    elif str(re.match("^\[([\w\d])+$", str(word))) != "None":
        retuxx = str(word).replace("[", "")
    elif str(re.match("^[b]\]([\w\d])+$", str(word))) != "None":
        retuxx = str(word).replace("b]", "")
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


arrayoffilteredsentences=[]

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
    i = str(i).replace('', " ")
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
        sentencestringfiltered = ""
        for x321 in re.split(" |,", ixre):
            sentencestringfiltered = sentencestringfiltered + " " + wordduplicationcheckatEnd(str(x321).strip())
        arrayoffilteredsentences.append(str(sentencestringfiltered))

    else:
        sentencestringfiltered = ""
        sentencestringfiltered = wordduplicationcheckatEnd(str(ixre).strip())
        arrayoffilteredsentences.append(str(sentencestringfiltered))





        # textreader = open("candidates.txt", 'r')
        #
        #
        # textreader.close()