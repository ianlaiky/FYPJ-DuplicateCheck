import os

try:

    os.mkdir("wordsSentenceAssignment")
except:
    pass

f = open("wordsSentenceAssignment\sentencesAssignment.txt", 'r', encoding="utf-8")
files = f.readlines()
f.close()

filecount = 0
for i in files:
    if str(i).strip() != "":
        if str(i).strip() != " ":
            # print(str(i).strip())
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

            print(str(i).strip()[str(i).index("|") + 2:])
            fi = open("..\..\sentencesInFiles\sentence_" + str(filecount) + ".txt", 'w', encoding="utf-8")
            fi.writelines(str(i).strip()[str(i).index("|") + 2:])
            fi.close()
            filecount = int(filecount) + 1
