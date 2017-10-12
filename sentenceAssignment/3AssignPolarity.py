
f = open("wordsSentenceAssignment\singlish_polarity_SVMresults_conf.txt",'r',encoding="utf-8")
file = f.readlines()
f.close()

polarityDict={}

for i in file:
    if str(i).strip()!="":
        if str(i).strip()!=" ":
            # print(str(i).strip())

            print(str(i).strip()[str(i).find("sentence_")+9:str(i).find(".txt")])
            print(str(i).strip()[str(i).find("conf(pos)=")+10:str(i).find("conf(neg)")-1])
            polarityDict[str(i).strip()[str(i).find("sentence_")+9:str(i).find(".txt")]]=str(i).strip()[str(i).find("conf(pos)=")+10:str(i).find("conf(neg)")-1]

# print(polarityDict[str("2")])



fout = open("wordsSentenceAssignment\sentencesAssignment.txt",'r',encoding="utf-8")
sentence=fout.readlines()
fout.close()


linescount=0
for o in sentence:
    if str(o).strip()!="":
        if str(o).strip()!=" ":
            # print(str(o).strip())
            print(str(o).strip()[str(o).index("|") + 2:])
            print(polarityDict[str(linescount)])
            linescount=int(linescount)+1

