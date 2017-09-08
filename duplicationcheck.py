from openpyxl import load_workbook

import fnmatch

# print(columnlist)

columnlist = []


# regex test
def excelinput(filetoeopn, filecheckksheets):
    # loading in workbook
    wb = load_workbook(filetoeopn)

    print("Sheets names:")
    # obtaining sheets names
    print(wb.get_sheet_names())
    sheet = wb[wb.get_sheet_names()[filecheckksheets]]

    #
    data = sheet.values

    # print(next(data)[0:])



    for r in data:
        # print(r[0])
        columnlist.append(r[0])


alllistarr = []


# for i in columnlist:
#     print(i)
def searchcase():
    for i in columnlist:
        # print(i)
        if fnmatch.fnmatch(str(i), "*" + userinput + "*"):
            alllistarr.append(i)
            # print(i)


def matchcase():
    for i in columnlist:
        # print(i)
        if fnmatch.fnmatch(str(i), userinput):
            alllistarr.append(i)
            # print(i)


excelinput('ner.xlsx', 0)
excelinput('singish.xlsx', 1)
userWeb=''



while(userWeb!="exit"):

    print("-----------------------------")
    userWeb = input("Enter 'exit' to exit"+"\n" +"Word duplication check:"+"\n")
    userinput = str(userWeb)

    if(userinput=="exit"):
        break

    matchorsearcase = input("Use Match or Search? m=Match, s=Search"+"\n")
    matchsc = str(matchorsearcase)

    if matchsc == "m":
        matchcase()
    elif matchsc == "s":
        searchcase()

    # searchcase()

    if (len(alllistarr) == 0):
        print("No match found")
    else:
        for i in alllistarr:
            print(i)
    print("**Records found: " + str(len(alllistarr))+"**")
    alllistarr.clear()
    print("Total records scanned: " + str(len(columnlist) - 1))


