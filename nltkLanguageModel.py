from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
word ="I found a wild animal by the zookeeper den"






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
                    wewe=myString[myString.index(startreadArea) + indextoadd:myString.index(endReadArea)].replace("_"," ")

                else:
                    pyarr.append(myString.replace("\n", ""))
        except:
            pass
    return pyarr


senticNetWords=pythonFile("filesdb\senticnet.py","['","']",2,"-----nil--------")
print(set(senticNetWords))

languages_ratios = {}
tokens = wordpunct_tokenize(word)

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


print(languages_ratios)