import urllib.request, json



f = open('dataset.txt', 'w', encoding="utf-8")
url="https://cache-api.ranker.com/lists/161641/items?limit=50&offset=150&include=votes,wikiText,rankings,openListItemContributors&propertyFetchType=ALL&liCacheKey=null"
with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())


    for index,ele in enumerate(data["listItems"]):

        print(data["listItems"][index]["node"]["name"])
        f.writelines(str(data["listItems"][index]["node"]["name"])+"\n")
f.close()