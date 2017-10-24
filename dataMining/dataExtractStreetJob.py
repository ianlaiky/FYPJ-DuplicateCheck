import re
import requests
from bs4 import BeautifulSoup
import os



try:

    os.mkdir("extractedData")
except:
    pass


alphabet="Z"
pagess=91



f = open("extractedData\ExtractedDataStreetJob="+str(alphabet)+".txt", 'w', encoding="utf8")





# f.writelines(str("dsd") + "\n\n")
headers = {'User-agent': 'Mozilla/5.0'}

# userWeb = input("Website: ")
userWeb = "http://www.streetdirectory.com/businessfinder/company/All/All/"+str(alphabet)+"/"
interation=1


sitesExtracted=[]

# print(soup)
# print(soup.find('class="listing_company_name"'))
# print(soup.find_all('a',{"class": "listing_company_name"}))
#
# print(soup.find_all('a',{"class": "listing_company_name"})[0].text)

for interationnn in range(pagess):
    website = str(userWeb)+str(interationnn)
    r = requests.get(website, headers=headers)
    data = r.text
    soup = BeautifulSoup(data, "lxml")

    for ux in soup.find_all('a',{"class": "listing_company_name"}):
        print(ux.text)
        sitesExtracted.append(ux.text)
        f.writelines(str(ux.text)+"\n")

textlist={}

# for links in range(946):
#     print(str(userWeb)+str(links))
#
#     r = requests.get(str(userWeb)+str(links), headers=headers)
#     data = r.text
#     soup = BeautifulSoup(data, "lxml")
#     for i in soup.find_all('div',{"class": "contenth3"}):
#         print(i.text)
#         print(i.find('a')['href'])
#         textlist[str(i.text).strip()]=str(i.find('a')['href'])
#         f.writelines(str(i.text).strip()+"\n")
#
#
# print(textlist)
# print(len(textlist))






f.close()


