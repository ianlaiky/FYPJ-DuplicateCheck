import re
from openpyxl import load_workbook


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
            columnlist.append(r[columnNo])

    return columnlist

# excelinput("datafiles\sgforums.xlsx",0,0)


class DataValue():
    def __init__(self, itemm, countt):
        self.item = itemm
        self.count = countt

    def getitem(self):
        return self.item

    def getitemCount(self):
        return self.countt
    def setitemCounr(self,itemm):
        self.item=itemm
        return self.item

listoflistobjects=[]
listtt=[]
listtt.append("testttttt")
listtt.append(0)
listoflistobjects.append(listtt)
def wordduplicationcheck(wordstocheck):
    wordcount=0
    templist=[]
    for i in listoflistobjects:
        if str(i[0])==wordstocheck:
            wordcount=wordcount+1
    if wordcount==0:
        if wordstocheck!="":
            templist.append(wordstocheck)
            templist.append(1)
            listoflistobjects.append(templist)
    else:
        for count,element in enumerate(listoflistobjects):
            if str(element[0])==wordstocheck:
                tempcont = listoflistobjects[count][1]
                listoflistobjects[count][1]=tempcont+1










f = open('test.txt','w',encoding="utf-8")




counttttt=0

for i in excelinput("datafiles\sgforums.xlsx",0,0):
    # print(i)
    print("Currently scanning Line: "+str(counttttt))
    counttttt=counttttt+1
    i=str(i).replace('\n'," ")
    i=str(i).replace('\\n'," ")
    i=str(i).lower()
    #do blank check to see if have space
    if str(i).find(" ")!=-1:
        for x in re.split(" |,",i):
            # print(x)
            # f.writelines(x+"\n")
            wordduplicationcheck(str(x).strip())
    else:
        wordduplicationcheck(str(i).strip())
        # f.writelines(str(i) + "\n")
    # except:
    #     pass
listoflistobjects.sort(key = lambda x: x[1],reverse=True)

for h in listoflistobjects:
    f.writelines(str(h[0])+"\t\t"+str(h[1])+"\n")




print(listoflistobjects)

f.close()