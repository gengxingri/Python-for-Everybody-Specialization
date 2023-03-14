#The program will use urllib to read the HTML from the data files below, 
#and parse the data, extracting numbers and compute the sum of the numbers in the file.
#Actual data: http://py4e-data.dr-chuck.net/comments_1466062.html


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
count=0
sum=0
tags = soup('span')
for tag in tags:
    count+=1
    num=int(tag.contents[0])
    sum+=num
print('count', count)
print('sum', sum)
