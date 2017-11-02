from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from openpyxl import load_workbook
import os

word =""




f = open('SinglishSentencesForNer.txt', 'w', encoding="utf-8")

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
                    pyarr.append(
                        (str(myString[myString.index(startreadArea) + indextoadd:myString.index(endReadArea)]).lower().replace("_"," ")))

                else:
                    pyarr.append(myString.replace("\n", ""))
        except:
            pass
    return pyarr

#read in

    print(inread)



senticNetWords=pythonFile("..\\filesdb\senticnet.py","['","']",2,"-----nil--------")
# print(senticNetWords)
print(set(senticNetWords))

languages_ratios = {}



for inread in excelinput("..\datafiles\Edmwcompiled311017.xlsx",0,0):
    tokens = wordpunct_tokenize(inread)

    words = [word.lower() for word in tokens]


    # list of sets of stopwords for each language
    dictOfSetsOfStopwords={}
    languages_ratios={}

    dictOfSetsOfStopwords["singlish"]=set(senticNetWords)
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        dictOfSetsOfStopwords[language]=stopwords_set


    for eachLan in dictOfSetsOfStopwords:
        # print(dictOfSetsOfStopwords[eachLan])
        corpusSet = set(words)
        common_elements = corpusSet.intersection(dictOfSetsOfStopwords[eachLan])
        languages_ratios[eachLan]=len(common_elements)


    # print(languages_ratios)
    # print(languages_ratios["singlish"])

    if int(languages_ratios["singlish"])>1:
        print(str(inread).strip())

        f.writelines(inread)
f.close()