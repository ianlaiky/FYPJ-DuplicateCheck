
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


fintake=open("wordsSentenceAssignment\sentencesAssignmentWithPolarity.txt",'w',encoding="utf-8")

linescount=0
for o in sentence:
    if str(o).strip()!="":
        if str(o).strip()!=" ":
            # print(str(o).strip())
            print(str(o).strip()[str(o).index("|") + 2:])
            print(polarityDict[str(linescount)])

            if float(polarityDict[str(linescount)])>0.7 or float(polarityDict[str(linescount)])<0.3:
                fintake.writelines(str(o).strip()+"\n")
                fintake.writelines("*High Polarity*"+"\n\n")
                # fintake.writelines("Negative Polarity: "+str(polarityDict[str(linescount)])+"\n\n")
            else:
                fintake.writelines(str(o).strip() + "\n")
                fintake.writelines("Netural Polarity" + "\n\n")

            linescount=int(linescount)+1


fintake.close()