import urllib.request, json



f = open('dataset.txt', 'w', encoding="utf-8")


with urllib.request.urlopen("https://cache-api.ranker.com/lists/161641/items?limit=50&offset=100&include=votes,wikiText,rankings,openListItemContributors&propertyFetchType=ALL&liCacheKey=null") as url:
    data = json.loads(url.read().decode())


    for index,ele in enumerate(data["listItems"]):

        print(data["listItems"][index]["node"]["name"])
        f.writelines(str(data["listItems"][index]["node"]["name"]))
f.close()