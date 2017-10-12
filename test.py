import re
from openpyxl import load_workbook

import fnmatch


# import enchant
#
# d = enchant.Dict("en_US")
# de = enchant.Dict("en_GB")
#
# print(d.check("cool"))
# print(de.check("on-line"))
# print(de.check("afk"))

# if d.check("running") is True:
#     print("ts")

# import unicodedata
#
# def normalize_caseless(text):
#     return unicodedata.normalize("NFKD", text.casefold())
#
# def caseless_equal(left, right):
#     return normalize_caseless(left) == normalize_caseless(right)
#
# print(caseless_equal("james" ,"Jamess"))



# import re
# from openpyxl import load_workbook
# from collections import Counter
#
#
# def excelinput(filetoeopn, filecheckksheets, columnNo):
#     columnlist = []
#     # loading in workbook

#     wb = load_workbook(filetoeopn)
#
#     print("Sheets names:")
#     # obtaining sheets names
#     print(wb.get_sheet_names())
#     sheet = wb[wb.get_sheet_names()[filecheckksheets]]
#
#     #
#     data = sheet.values
#
#     for r in data:
#         # print(r[0])
#         if r[columnNo] is not None:
#             # print(r[columnNo])
#             columnlist.append(r[columnNo])
#
#     return columnlist
#
# for i in excelinput("datafiles\sgforums.xlsx", 0, 0):
#     if re.search("don",str(i))!="None":
#         print(i)
#
# x = '197a0"'
# x1 = "2)dsad"
# x2 = "3)dasasad"
# y = "3"
#
# print(x)
# print(re.match("^([\w])+\"$", x))

# x="asdsadsad fdsghgd haha"
# print(x.find("hahads"))

# if x.startswith('‘'):
#     print("work")




# y="text,,,0"
# x="(pp)"
# x1=""
# x2=""
# print(y.split(","))
#
# print(x[x.index(y.split(",")[1])+int(y.split(",")[3]):x.index(y.split(",")[2])])

# word = "James John"
# allword = word.split(" ")
# firstword=allword[0]
#
# x = ['James', "John", 'Peter', 'Le', 'has']
#
# # print(x.index("Peter"))
# if str(x[x.index(firstword)] + " " + x[x.index(firstword) + 1]) == word:
#     print(x[x.index(firstword)]+" "+x[x.index(firstword) + 1])
#     print(x.index(firstword))
#     print("Found")

# testarr = []
# stopword = ["a","i'll","the"]
#
# x = "whiat the games ass | a d asd the sd s/ads i'll fdsf ds.fcdsfs,     fsdf ds     fdsf"
#
# sentence=""
# for te in x.split(" "):
#     if str(te)!="":
#         if str(te)!=" ":
#             wordcount = 0
#             for qwe in stopword:
#
#                 print(te.strip())
#                 if str(re.match("^("+str(qwe)+")$", str(te).strip()))!="None":
#                     temp=str(te).replace(qwe, "")
#                     sentence=str(sentence)+" "+str(temp).strip()
#                     wordcount=wordcount+1
#             if wordcount==0:
#                 sentence = str(sentence) + " " + str(te).strip()
#             else:
#                 print("gdfg")
#
#
#
# print(sentence)



# for x1 in x.split(""):
#     if str(x1) != "":
#         if str(x1) != " ":
#             print(x1)
#             x1 = re.sub('\s+', ' ', x1).strip()
#             testarr.append(x1.strip())
#
# print(testarr)




# print(testarr)


# def excelinput(filetoeopn, filecheckksheets, columnNo):
#     columnlist = []
#     # loading in workbook
#     wb = load_workbook(filetoeopn)
#
#     print("Sheets names:")
#     # obtaining sheets names
#     print(wb.get_sheet_names())
#     print("Sheets Loaded: " + wb.get_sheet_names()[filecheckksheets])
#     sheet = wb[wb.get_sheet_names()[filecheckksheets]]
#
#     #
#     data = sheet.values
#
#     # print(next(data)[0:])
#
#     for r in data:
#         # print(r[0])
#         columnlist.append(r[columnNo])
#
#     return columnlist
#
# counttttt = 0
#
# currentFileNo=0
#
# for i in excelinput("datafiles\sgforums.xlsx", 0, 0):
#     if str(i) != "None":
#
#         print("Currently scanning Line: " + str(counttttt))
#         counttttt = counttttt + 1
#         i = str(i).replace('\n', " ")
#         i = str(i).replace('\\n', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#         i = str(i).replace('', " ")
#
#         i = str(i).replace('…', '...')
#         print(i)
#
#         f = open("..\sentencesInFiles\sentence_"+str(currentFileNo)+".txt","w", encoding="utf-8")
#         f.writelines(str(i))
#         f.close()
#         currentFileNo=int(currentFileNo)+1
#
# x = "0.78"
#
# x=float(x)+1
#
# print(x)

# x = "0/2"
#
# print(x[:str(x).index("/")])
# print(x[str(x).index("/")+1:])

# x="jamie le"
#
# print(x.fe le"
#
# print(x.find("jami4"))