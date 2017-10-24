import re
import requests
from bs4 import BeautifulSoup
import os



try:

    os.mkdir("extractedData")
except:
    pass
f = open("extractedData\ExtractedData.txt", 'w', encoding="utf8")


# f.writelines(str("dsd") + "\n\n")
headers = {'User-agent': 'Mozilla/5.0'}

# userWeb = input("Website: ")
userWeb = "http://www.timesbusinessdirectory.com/company/list/all/"
interation=1
web2="http://www.timesbusinessdirectory.com/company"

# r = requests.get(userWeb, headers=headers)
# data = r.text
# soup = BeautifulSoup(data, "lxml")

# print(soup.find('class="container"'))
# print(soup.find_all('div',{"class": "contenth3"}))


textlist={}

for links in range(946):
    print(str(userWeb)+str(links))

    r = requests.get(str(userWeb)+str(links), headers=headers)
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    for i in soup.find_all('div',{"class": "contenth3"}):
        print(i.text)
        print(i.find('a')['href'])
        textlist[str(i.text).strip()]=str(i.find('a')['href'])
        f.writelines(str(i.text).strip()+"\n")


print(textlist)
print(len(textlist))





# for opppp in textlist:
#     f.writelines(str(opppp)+"\n\n")


f.close()


