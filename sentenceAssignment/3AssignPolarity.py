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

fintake = open("wordsSentenceAssignment\SecondsentencesAssignmentWithPolarity.txt", 'w', encoding="utf-8")

dictforword = {}
dictforwordPositive = {}
dictforwordNegative = {}

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

            if str(o).strip()[:str(o).index("|") - 1] not in dictforwordPositive:
                dictforwordPositive[str(o).strip()[:str(o).index("|") - 1]] = "0/0"

            percent = dictforword[str(o).strip()[:str(o).index("|") - 1]]
            firstpercent = str(percent[:str(percent).index("/")])
            secondpercent = str(percent[int(str(percent).index("/")) + 1:])
            positivity = int(str(dictforwordPositive[str(o).strip()[:str(o).index("|") - 1]][
                                 :str(dictforwordPositive[str(o).strip()[:str(o).index("|") - 1]]).index("/")]))
            # negativity=int(str(dictforwordPositive[i][int(str(dictforwordPositive[i]).index("/")) + 1:]))

            if float(polarityDict[str(linescount)]) > 0.6 or float(polarityDict[str(linescount)]) < 0.4:
                # print(float(polarityDict[str(linescount)]))
                if float(polarityDict[str(linescount)]) < 0.4:
                    positivity = int(positivity) + 1
                    # print("DDDDDDDDDDDDDDDDDDD")
                # if float(polarityDict[str(linescount)]) > 0.6:
                #     # negativity = int(negativity) + 1
                firstpercent = int(firstpercent) + 1
                secondpercent = int(secondpercent) + 1

                fintake.writelines(str(o).strip() + "\n")
                fintake.writelines("Negative Polarity: " + str(polarityDict[str(linescount)]) + "\n")
                fintake.writelines("Polarity*" + "\n\n")
            else:

                secondpercent = int(secondpercent) + 1
                fintake.writelines(str(o).strip() + "\n")
                fintake.writelines("Negative Polarity: " + str(polarityDict[str(linescount)]) + "\n")
                fintake.writelines("Netural Polarity" + "\n\n")
            dictforword[str(o).strip()[:str(o).index("|") - 1]] = str(firstpercent) + "/" + str(secondpercent)

            dictforwordPositive[str(o).strip()[:str(o).index("|") - 1]] = str(positivity) + "/" + str(firstpercent)
            # dictforwordNegative[str(o).strip()[:str(o).index("|") - 1]] = str(negativity) + "/" + str(firstpercent)

            linescount = int(linescount) + 1
            print(linescount)

listofwordstosave = []
netrualwords = []

for x in dictforword:
    per = dictforword[x]
    firstper = per[:str(per).index("/")]
    secper = per[int(str(per).index("/")) + 1:]
    if int(firstper) / int(secper) > 0.6:
        listofwordstosave.append(str(x))
        print(x)
    else:
        print("Neutral")
        print(x)
        netrualwords.append(x)
# print(dictforword["fokkers"])

fintake.close()
finsave = open("wordsSentenceAssignment\ThirdFilteredsentencesAssignmentWithPolarity.txt", 'w', encoding="utf-8")

for oi in sentence:
    if str(oi).strip() != "":
        if str(oi).strip() != " ":
            for oii in listofwordstosave:
                if str(oi).strip()[:str(oi).index("|") - 1] == str(oii):
                    finsave.writelines(oi + "\n")

finsave.close()
# print("Net")
# print(netrualwords)
# print(len(netrualwords))

print(dictforword)
print(dictforwordPositive)
print(len(dictforwordPositive))
# print(dictforwordNegative)
# print(len(dictforwordNegative))
print(dictforword["mps"])

fextremePolarity = open("wordsSentenceAssignment\FourthFilteredsentencesAssignmentWithPolarity.txt", 'w',
                        encoding="utf-8")

# savethewordsforin=[]

for lala in listofwordstosave:
    fextremePolarity.writelines("Candidates " + lala + "\n")
    # print(dictforwordPositive[lala])
    firstpos = str(dictforwordPositive[lala][:int(str(dictforwordPositive[lala]).find("/"))])
    secpos = str(dictforwordPositive[lala][int(str(dictforwordPositive[lala]).find("/")) + 1:])
    # print(firstpos)
    # print(secpos)

    percentage = round((int(firstpos) / int(secpos)) * 100, 2)

    fextremePolarity.writelines("Positivity: " + str(percentage) + "%" + "\n\n")

# for i in dictforwordPositive:
#     print(dictforwordPositive[i])
#     print(int(str(dictforwordPositive[i][:str(dictforwordPositive[i]).index("/")])))
#     print(int(str(dictforwordPositive[i][int(str(dictforwordPositive[i]).index("/")) + 1:])))
#
#     try:
#         extremePercent = int(str(dictforwordPositive[i][:str(dictforwordPositive[i]).index("/")])) / int(str(dictforwordPositive[i][int(str(dictforwordPositive[i]).index("/")) + 1:]))
#     except:
#         extremePercent=-1
#         pass
#
#     if float(extremePercent)>0.7 or float(extremePercent)<0.3:
#         print("Candidates "+str(i))
#         # fextremePolarity.writelines("Candidates "+str(i)+"\n\n")
#         savethewordsforin.append(str(i))
# realsave=list(set(savethewordsforin).intersection(listofwordstosave))
# for all in sentence:
#     if str(all).strip() != "":
#         if str(all).strip() != " ":
#             # print(str(o).strip())
#             print(str(all).strip()[str(all).index("|") + 2:])
#             # print(str(o).strip()[:str(o).index("|") -1])
#
#
#             if str(all).strip()[:str(all).index("|") - 1] in realsave:
#                 fextremePolarity.writelines(str(all)+ "\n")
#
# print(len(realsave))

fextremePolarity.close()
