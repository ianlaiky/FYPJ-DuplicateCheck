f = open("wordsSentenceAssignment\singlish_polarity_SVMresults_conf.txt", 'r', encoding="utf-8")
file = f.readlines()
f.close()

polarityDict = {}

for i in file:
    if str(i).strip() != "":
        if str(i).strip() != " ":
            # print(str(i).strip())

            print(str(i).strip()[str(i).find("sentence_") + 9:str(i).find(".txt")])
            print(str(i).strip()[str(i).find("conf(pos)=") + 10:str(i).find("conf(neg)") - 1])
            polarityDict[str(i).strip()[str(i).find("sentence_") + 9:str(i).find(".txt")]] = str(i).strip()[str(i).find(
                "conf(pos)=") + 10:str(i).find("conf(neg)") - 1]

# print(polarityDict[str("2")])



fout = open("wordsSentenceAssignment\sentencesAssignment.txt", 'r', encoding="utf-8")
sentence = fout.readlines()
fout.close()

fintake = open("wordsSentenceAssignment\sentencesAssignmentWithPolarity.txt", 'w', encoding="utf-8")

dictforword = {}

linescount = 0
for o in sentence:
    if str(o).strip() != "":
        if str(o).strip() != " ":
            # print(str(o).strip())
            print(str(o).strip()[str(o).index("|") + 2:])
            # print(str(o).strip()[:str(o).index("|") -1])
            print(polarityDict[str(linescount)])

            if str(o).strip()[:str(o).index("|") - 1] not in dictforword:
                dictforword[str(o).strip()[:str(o).index("|") - 1]] = "0/0"
            percent = dictforword[str(o).strip()[:str(o).index("|") - 1]]
            firstpercent = str(percent[:str(percent).index("/")])
            secondpercent = str(percent[int(str(percent).index("/")) + 1:])
            if float(polarityDict[str(linescount)]) > 0.7 or float(polarityDict[str(linescount)]) < 0.3:

                secondpercent=int(secondpercent)+1



                fintake.writelines(str(o).strip() + "\n")
                fintake.writelines("Negative Polarity: "+str(polarityDict[str(linescount)])+"\n")
                fintake.writelines("Polarity*" + "\n\n")
            else:
                firstpercent = int(firstpercent) + 1
                secondpercent = int(secondpercent) + 1
            fintake.writelines(str(o).strip() + "\n")
            fintake.writelines("Negative Polarity: " + str(polarityDict[str(linescount)]) + "\n")
            fintake.writelines("Netural Polarity" + "\n\n")
            dictforword[str(o).strip()[:str(o).index("|") - 1]]=str(firstpercent)+"/"+str(secondpercent)


            linescount = int(linescount) + 1
            print(linescount)

listofwordstosave=[]
netrualwords=[]

for x in dictforword:
    per = dictforword[x]
    firstper= per[:str(per).index("/")]
    secper= per[int(str(per).index("/"))+1:]
    if int(firstper)/int(secper) >0.6:
        listofwordstosave.append(str(x))
        print(x)
    else:
        print("Neutral")
        print(x)
        netrualwords.append(x)
# print(dictforword["fokkers"])

fintake.close()
finsave = open("wordsSentenceAssignment\FilteredsentencesAssignmentWithPolarity.txt", 'w', encoding="utf-8")

for oi in sentence:
    if str(oi).strip() != "":
        if str(oi).strip() != " ":
            for oii in listofwordstosave:
                if str(oi).strip()[:str(oi).index("|") - 1]==str(oii):
                    finsave.writelines(oi+"\n")
print("Net")
print(netrualwords)
print(len(netrualwords))









finsave.close()


