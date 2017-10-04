import re

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

testarr=[]
stopword=["|","/",".",","]

x="what the games ass|d asd sd s/ads fdsf ds.fcdsfs,     fsdf ds     fdsf"


for wor in stopword:
    x=x.replace(wor,"")


for x1 in x.split(""):
    print(x1)
    x1=re.sub('\s+', ' ', x1 ).strip()
    testarr.append(x1.strip())

print(testarr)



# print(testarr)
