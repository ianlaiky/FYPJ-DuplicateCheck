import re
import requests
from bs4 import BeautifulSoup
import os

headers = {'User-agent': 'Mozilla/5.0'}

# userWeb = input("Website: ")
userWeb = "http://www.timesbusinessdirectory.com/company/details/80099338/innoflex-pte-ltd"
# web2="http://www.timesbusinessdirectory.com/company"

r = requests.get(userWeb, headers=headers)
data = r.text
soup = BeautifulSoup(data, "lxml")


# print(soup)

# print(soup.find('class="container"'))

# print(str(soup.find('span',{"class": "coprofileh3"}).find_parent()).strip())



inner_text = soup.find('span',{"class": "coprofileh3"}).find_parent()


decomposingthis=inner_text.find('span')
decomposingthis.decompose()


# print(str(inner_text.renderContents()).strip())
gammm = str(inner_text.renderContents()).strip()
gammm = str(gammm).replace("\\r","")
gammm = str(gammm).replace("\\n","")
gammm = str(gammm).replace("\\t","")
gammm = str(gammm).replace("b'","")

print(gammm.split("<br/>")[4])
print(gammm.split("<br/>")[5])
print(gammm.split("<br/>")[6])

# for breaks in gammm.split("<br/>"):
#
#             print(breaks)


# print(inner_text)

# print(inner_text.find(style="padding-left: 15px;"))
# print(inner_text.find('td'))

textlist={}

#
# for i in soup.find_all('div',{"class": "contenth3"}):
#     print(i.text)
#     print(i.find('a')['href'])
#     textlist[str(i.text).strip()]=str(i.find('a')['href'])
#
#
# print(textlist)



# for link in soup.find_all("container"):
#     print(link)

# image = link.get("src")
# imag = image.replace("image", "original")
# # print(imag.find("http"))
# if(imag.find("http://cfile")==0):
#     print(imag)
#
#     imgSplit=os.path.split(imag)
#     if (imgSplit[1][-3:]!="gif"):
#         imgNam = imgSplit[1]+".jpg"
#     else:
#         imgNam = imgSplit[1]
#     r2=requests.get(imag,headers=headers)
#     # print(imgNam)
#     with open(imgNam,"wb") as f:
#         f.write(r2.content)
#
