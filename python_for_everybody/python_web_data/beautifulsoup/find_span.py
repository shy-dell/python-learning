import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

lst = []
tags = soup('span')

# This was another option using some other functionality in beautifulsoup
'''for tag in tags:
    lst.append(int(tag.get_text()))'''

for tag in tags:
    lst.append(int(tag.string))

print(sum(lst))

