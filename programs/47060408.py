# from bs4 import BeautifulSoup

# url = 'insert your url here2'

# with open('file.html','r') as f:
#     text = f.read()

# soup = BeautifulSoup(text,'html.parser')

# soup.body.iframe['src'] = url

# with open('file.html','w') as f:
#     f.write(str(soup))


retval = ""
HTML_page = open('file.html','r')
LINK = 'google.com'

for item in HTML_page.readlines():
    if "<iframe src" in item:
        item = item.format(LINK)
    retval += item

HTML_page.close()
print(retval)