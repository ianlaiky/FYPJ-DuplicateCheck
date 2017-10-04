import re
from openpyxl import load_workbook
from collections import Counter
import enchant
import unicodedata

filestoOpen="microtext"

confff = open("../nodupefound.txt", 'r', encoding="utf-8")
conf = confff.readlines()
confff.close()

wordsFreq={}
currentword=""
for lines in conf:



    if str(lines)!="":
        if str(lines)!=" ":
            if str(lines).find("Word: ")!=-1:
                word=str(lines).replace("Word: ","")
                if str(word).find("|")!=-1:

                    # print(str(word[:word.find("|")]).strip())
                    currentword=str(word[:word.find("|")]).strip()
                else:
                    # print(str(word).strip())
                    currentword = str(word[:word.find("|")]).strip()

            elif str(lines).find("Frequency: ")!=-1:
                freq = str(lines).replace("Frequency: ", "")
                print(str(freq).strip())
                print(currentword)
                wordsFreq[currentword] = str(freq).strip()

print(wordsFreq)


f = open(filestoOpen+".txt", 'r', encoding="utf-8")
conf = f.readlines()
f.close()


fout = open("wordsWithFrequency\\"+filestoOpen+"Frequency.txt", 'w', encoding="utf-8")


for words in conf:
    if str(words)!="":
        if str(words)!=" ":

            # print(str(words).strip())
            fout.writelines("Words: "+str(words).strip()+"\n")
            fout.writelines("Frequency: "+wordsFreq[str(words).strip()]+"\n\n")




fout.close()