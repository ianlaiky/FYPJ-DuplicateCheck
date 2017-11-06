import urllib.request, json
with urllib.request.urlopen("https://cache-api.ranker.com/lists/161641/items?limit=50&offset=100&include=votes,wikiText,rankings,openListItemContributors&propertyFetchType=ALL&liCacheKey=null") as url:
    data = json.loads(url.read().decode())


    for index,ele in enumerate(data["listItems"]):

        print(data["listItems"][index]["node"]["name"])