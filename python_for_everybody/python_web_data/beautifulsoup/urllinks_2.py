import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL ")
#were going to assume the user inputs an appropriate number
link_num = input("What link do you want to follow (input a number greater than 0)? ")
rpt_num = input("And how many times should I repeat this process? ")
count = 0

while int(rpt_num) > count:
    url = url
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[int(link_num)-1].get('href', None)
    # index will be 1 less than the position that the user inputs
    count += 1

    print(f"Retriving: {url}")

x = re.findall(r"known_by_(\w+).html",url)
print(x[0])