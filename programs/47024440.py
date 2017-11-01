import requests, pprint
from bs4 import BeautifulSoup
music = []
page_url = "http://waterflame.newgrounds.com/audio/"
page = requests.get(page_url)
soup = BeautifulSoup(page.text, "html.parser")
allTags = soup.find_all('a')
print(allTags)
for tag in allTags:
    toCheck = "www.newgrounds.com/audio/listen/"
    if toCheck in tag:
        music.append([tag.get("href"),tag.contents])
    #pprint.pprint(music)
