import xlsxwriter as xlsxwriter

import re
from openpyxl import load_workbook
from collections import Counter
import enchant
import unicodedata

from langdetect import detect, DetectorFactory


DetectorFactory.seed = 0


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
            columnlist.append(str(r[columnNo]))

    return columnlist


sentenceCount = 0

sgenCount = 0

fsaveSinglish = open("SinglishSentences.txt", 'w', encoding="utf-8")
ffailedDetect = open("FailedSentences.txt", 'w', encoding="utf-8")

languages_ratios = {}
row = 0
col = 0
workbook = xlsxwriter.Workbook('DatabaseForLangdetect.xlsx')
worksheet = workbook.add_worksheet()

for i in excelinput("..\datafiles\Edmwcompiled311017.xlsx", 0, 0):

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
    print(str(i).strip())
    # print(detect(i))

    print("Sentence No: " + str(sentenceCount))
    try:

        if str(detect(str(i).strip())) == "sgen":
            # print("Acceptec")
            fsaveSinglish.writelines(str(i).strip() + "\n\n")
            sgenCount = sgenCount + 1
            worksheet.write(row, col, str(i).strip())
            row += 1
    except:
        ffailedDetect.writelines(str(i).strip() + "\n\n")
        pass

    sentenceCount = sentenceCount + 1
print("Singlish sentences: " + str(sgenCount) + "/" + str(sentenceCount))

# print(detect('Have you eaten?'))
# print(detect_langs('Dont be in like this way'))
workbook.close()
fsaveSinglish.close()
ffailedDetect.close()

# forum data for reading
forumdataforreading = "DatabaseForLangdetect.xlsx"

stopwordsseperator = []
stopwordsseperatorNER = []

stopwirdin = open('..\\filesdb\Seperator\stopwordSeperator.txt', 'r', encoding="utf-8")

stopwilala = stopwirdin.readlines()

for readlinesstopwoird in stopwilala:
    stopwordsseperator.append(str(readlinesstopwoird).lower().strip())

print(stopwordsseperator)
stopwirdin.close()

# stopwordinNER = open('..\\filesdb\Seperator\stopwordsLangDetect.txt', 'r', encoding="utf-8")
# stopNERreadline = stopwordinNER.readlines()
# for wordReadLine in stopNERreadline:
#     stopwordsseperatorNER.append(str(wordReadLine).lower().strip())
# print(stopwordsseperatorNER)
# stopwordinNER.close()


def excelinputRe(filetoeopn, filecheckksheets, columnNo):
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
            columnlist.append(str(r[columnNo]).lower().strip())

    return columnlist


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
            columnlist.append(str(r[columnNo]))

    return columnlist


# comparing 2 words: https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison-in-python
def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())


def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)


tempppppaarrrrr = []


# punctuation remover
def multiplepunctuationRemover(words):
    # line32 = re.sub('\.\.+', ' ', words)
    line32 = re.sub('\!!+', ' ', words)
    line32 = re.sub('\?\?+', ' ', line32)
    line32 = re.sub('\-\-+', ' ', line32)
    line32 = re.sub('\_\_+', ' ', line32)
    line32 = re.sub('\=\=+', ' ', line32)

    # if str(re.match("^[aA-zZ]+\/[aA-zZ]+$", str(line))) != "None":
    #     line=line.replace("/"," ")

    return line32


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
            return (specificcharacterremoverandother(wordstocheck[0:-1]))
        else:
            return (specificcharacterremoverandother(wordstocheck))
    elif wordstocheck[-2:] == "'s":
        return (specificcharacterremoverandother(wordstocheck[0:-2]))
    elif wordstocheck[-2:] == "’s":
        return (specificcharacterremoverandother(wordstocheck[0:-2]))
    else:
        return (specificcharacterremoverandother(wordstocheck))


counttttt = 0

# RAW DATA HERE
for i in excelinput(forumdataforreading, 0, 0):
    # print("dsdsdsadsasadsadsadsadsdsadsdsa")
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

    i = str(i).replace('…', '...')

    i = str(i).replace('.', "")
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

    sentences = ""

    # .replace to fix Ellipsis problem
    if str(ixre).find(" ") != -1:
        for x321 in re.split(" |,", ixre):

            if str(x321) != "":
                if str(x321) != " ":
                    sentences = sentences + " " + wordduplicationcheckatEnd(str(x321).strip())
    else:

        sentences = sentences + " " + wordduplicationcheckatEnd(str(ixre).strip())
    # print(sentences)
    # print("fdf")
    # ngram stopword seperator
    # sentences=sentences.lower()
    asentencess = sentences
    for nerln in stopwordsseperatorNER:
        # print(nerln)
        if str(re.search("\\b(" + str(nerln) + ")\\b", str(asentencess).strip())) != "None":
            # print("yes")
            asentencess = str(asentencess).replace(str(nerln), "")
    # print(asentencess)
    # print("dssd")
    # input()


    sentencetosave = ""
    for te in asentencess.split(" "):
        te = str(te).lower()
        if str(te) != "":
            if str(te) != " ":
                wordcount = 0

                for nerln in stopwordsseperatorNER:
                    if str(re.search("\\b(" + str(nerln) + ")\\b", str(te).strip())) != "None":
                        # print(te)
                        te = str(te).replace(str(nerln), "")
                        # print(te)
                        # print("DSFDFDFDE")
                        sentencetosave = str(sentencetosave) + " " + str(te).strip()
                        wordcount = int(wordcount) + 1

                # print(te)
                for qwe in stopwordsseperator:
                    qwe = str(qwe).lower()

                    # print(te)
                    # print(te.strip())
                    if str(re.match("^(" + str(qwe) + ")$", str(te).strip())) != "None":
                        # print(qwe)
                        tempwordlaa = str(te).replace(qwe, "")
                        sentencetosave = str(sentencetosave) + " " + str(tempwordlaa).strip()
                        wordcount = int(wordcount) + 1
                if int(wordcount) == 0:
                    # print(wordcount)
                    sentencetosave = str(sentencetosave) + " " + str(te).strip()

    # print(sentencetosave)
    # input()

    for ghsplitted in sentencetosave.split(""):
        # print("SDS")
        #
        # print(ghsplitted)
        # input()
        if str(ghsplitted) != "":
            if str(ghsplitted) != " ":
                # print(ghsplitted)
                # if str(ghsplitted).find("") != -1:
                #
                #     for nersplitted in str(ghsplitted).split(""):
                #         if str(nersplitted) != "":
                #             if str(nersplitted) != " ":
                #                 # print("SDSsss")
                #                 # print(nersplitted)
                #                 tempppppaarrrrr.append(str(nersplitted).strip())
                tempppppaarrrrr.append(str(ghsplitted).strip())


                # tempppppaarrrrr.append(sentences)
print("Converting to lowercase...")
newtempppppaarrrrr = []
print(tempppppaarrrrr)
for ghty in tempppppaarrrrr:
    newtempppppaarrrrr.append(str(ghty).lower())

my_dict = Counter(newtempppppaarrrrr)
print(my_dict)

del my_dict[' ']
del my_dict['']

# total freq
f = open('LangDetectAllfreq.txt', 'w', encoding="utf-8")
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
    ef = open(filetoopen, 'r', encoding="utf8")
    message = ef.readlines()

    # print(message)
    ef.close()
    # print(message)
    for myString in message:
        # print(myString)

        try:
            if myString.find(wordstoignore) == -1:
                if startreadArea != "":
                    pyarr.append(
                        (myString[myString.index(startreadArea) + indextoadd:myString.index(endReadArea)]).lower())
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
                                phoneticarr.append(str(re).lower())

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

confff = open("configLangDetect.txt", 'r')
conf = confff.readlines()
confff.close()

for i in conf:
    if i[:1] != "#":
        x = i.split(",")[0].strip()
        print(x)
        if x == "xlsx":
            # print("Value check to be deleteed(): "+str(i.split(",")[1].strip())+str(i.split(",")[2].strip())+str(i.split(",")[3].strip()))
            arrofileobjects.append(Files(i.split(",")[1].strip(),
                                         excelinputRe(i.split(",")[1].strip(), int(i.split(",")[2].strip()),
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
    # print(i.getArray())

userWeb = ''
userinput = ''
fdup = open('LangDetectdupefound.txt', 'w', encoding="utf-8")
fnodup = open("LangDetectANodupefound.txt", 'w', encoding="utf-8")
fnodupWithSomeExisting = open("LangDetectANodupefoundWithExistingSinglish.txt", 'w', encoding="utf-8")
# fnodupwspecial = open("ANodupefoundSpecialCharacter.txt", 'w', encoding="utf-8")

# for x in range(100):
#     fnodup.writelines("duhhh"+"\n")

my_dicInArray = []

parseinDict = {}
parseinDictDiff = {}

listOfAllThingsOfCurrDict = []

for index, abc in enumerate(my_dict):
    wordsfoundaryyyy = []
    print("Scanning: " + str(index) + "/" + str(len(my_dict)) + "\t" + str(
        round(int(index) / int(len(my_dict)) * 100, 2)) + "% Completed")
    sabc = str(abc).lower()
    my_dicInArray.append(sabc)

for c in arrofileobjects:
    print("Processing File: " + str(c.getFilename()))
    listOfAllThingsOfCurrDict = listOfAllThingsOfCurrDict + c.getArray()
    # print(c.getArray())
    # listyincheck = []

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
                               '€ڰ:', '_', '#', '?"', '<', '~', "'')", '?;', '=>', ':-', '.;', '?)', '{', '}', '!"',
                               '!=', '";', '/b]']

    languageToIgnore = ['ko', 'zh-cn', 'zh-tw', 'ja']

    returnvalue = True
    detectoinReceiver = "NIL"

    try:
        detectoinReceiver = str(detect(str(word))).lower()
    except:
        pass

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
    elif str(re.match("^([\w]+)\s+(wrote)$", str(word))) != "None":
        returnvalue = False

    elif detectoinReceiver in languageToIgnore:
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


def savingRegexExp(enteringWord):
    returnthis = False

    return returnthis


# sort special char to diff file, save all non-dup to one file
for ixxx in sorted(parseinDictDiff, key=parseinDictDiff.get, reverse=True):
    # ixxx = str(specificcharacterremoverandother(ixxxo))
    if dictus.check(ixxx) is False:
        if dictgb.check(ixxx) is False:
            tempwordthatl = ""
            # variation assignment
            try:
                tempwordthatl = str(tempwordthatl) + "  " + str(
                    verynewtempppppaarrrrr[uniqueverynewtempppppaarrrrr.index(ixxx.lower())])
            except:
                print("not: " + str(ixxx))
                pass

            line = re.search('[^A-Za-z]', str(ixxx))
            # print(line)
            # if 'None' != str(line):
            # if characterinvalidationchecker(str(ixxx).strip()) is True:
            # (variant assignment) start word check upper and lower case and end to variants list (*performance issue)

            # for checkkwor in tempppppaarrrrr:
            #     if caseless_equal(str(checkkwor), str(ixxx)) is True:
            #         tempwordsthatonlyrunperword = str(tempwordsthatonlyrunperword) + " / " + str(checkkwor)
            # end upper lower check

            # new test
            #
            # fnodupwspecial.writelines("Word: " + str(ixxx) + " " + str(tempwordthatl) + "\n")
            # fnodupwspecial.writelines("Frequency: " + str(my_dict[ixxx]) + "\n\n")

            # for chhs in tempppppaarrrrr:
            #     if caseless_equal(str(chhs),str(ixxx)) is True:
            #         tempwordthatl=str(tempwordthatl)+" / "+str(chhs)

            # new test
            if characterinvalidationchecker(str(ixxx).strip()) is True:

                incount = 0
                for xiccc in listOfAllThingsOfCurrDict:
                    # print(str("jalan jalan") in listOfAllThingsOfCurrDict)
                    # regexOutput = "None"
                    # try:
                    #     regexOutput = str(re.search("\\b(" + str(xiccc) + ")\\b", str(ixxx).strip()))
                    #
                    # except:
                    #     pass
                    #
                    # # print(xiccc)
                    # if str(regexOutput) != "None":
                    #     print("HELLLOOOO" + str(xiccc))
                    #     incount = incount + 1
                    #     break

                    eachword = 0
                    for incheckpls in str(xiccc).split(" "):
                        if incheckpls in str(ixxx).split(" "):
                            eachword = eachword + 1
                    if int(eachword) == len(str(xiccc).split(" ")):



                        print("works")
                        incount = 1

                print(str(ixxx) + str(incount))
                # print(incount)
                if incount == 0:

                    fnodup.writelines("Word: " + str(ixxx) + " " + str(tempwordthatl) + "\n")
                    fnodup.writelines("Frequency: " + str(my_dict[ixxx]) + "\n\n")



                else:

                    fnodupWithSomeExisting.writelines("Word: " + str(ixxx) + " " + str(tempwordthatl) + "\n")
                    fnodupWithSomeExisting.writelines("Frequency: " + str(my_dict[ixxx]) + "\n\n")

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
# fnodupwspecial.close()

#congratulations! you have reached the end :)