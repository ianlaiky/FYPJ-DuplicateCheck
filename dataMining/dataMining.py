# import re
# import requests
# from bs4 import BeautifulSoup
# import os
# headers = {'User-agent': 'Mozilla/5.0'}
#
# # userWeb = input("Website: ")
# userWeb = "https://search.insing.com/singapore/browse/art-galleries"
#
# r = requests.get(userWeb, headers=headers)
# data = r.text
# soup = BeautifulSoup(data, "lxml")
#
# # print(soup.find('class="container"'))
# print(soup)


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
