import re
# import enchant
# d = enchant.Dict("en_US")
# de = enchant.Dict("en_GB")
# print(d.check("america"))
# # print(de.check("afk"))
#
# if d.check("americans") is True:
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
x="(dsa"
x1="2)dsad"
x2="3)dasasad"
y="3"

print(re.match("(^\()([aA-zZ])+$",x))

print("\\")




# y="text,,,0"
# x="(pp)"
# x1=""
# x2=""
# print(y.split(","))
#
# print(x[x.index(y.split(",")[1])+int(y.split(",")[3]):x.index(y.split(",")[2])])

