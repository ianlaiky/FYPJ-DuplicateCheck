
f = open("wordsSentenceAssignment\sentencesAssignment.txt",'r', encoding="utf-8")
files = f.readlines()
f.close()

for i in files:
    if str(i).strip() !="":
        if str(i).strip() !=" ":
            # print(str(i).strip())

            print(str(i)[str(i).index("|")+2:])

