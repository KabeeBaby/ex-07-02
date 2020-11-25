#Done by Kaleb Hyde, Logan Yeubanks


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Deimante.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
for i in range(0,7):
    tags = soup("a")
    tag = tags[17]
    link = tag.get("href")
    html = urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    print(tag)
print("done")
