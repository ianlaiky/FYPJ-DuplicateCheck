
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
listtt.append()
def wordduplicationcheck(wordstocheck):
    wordcount=0
    templist=[]
    for i in listoflistobjects:
        if str(i[0])==wordstocheck:
            wordcount=wordcount+1
    if wordcount==0:
        templist.append(wordstocheck,1)
    # else:










f = open('test.txt','w',encoding="utf-8")






for i in excelinput("datafiles\sgforums.xlsx",0,0):
    print(i)
    # try:
    # f.writelines(str(i)+"\n")
    # except:
    #     pass
    # try:

    #do blank check to see if have space
    if str(i).find(" ")!=-1:
        for x in i.split(" "):
            print(x)
            f.writelines(x+"\n")
    else:
        f.writelines(str(i) + "\n")
    # except:
    #     pass



f.close()