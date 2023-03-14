
#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
#scan for a tag that is in a particular position relative to the first name in the list, 
#follow that link and repeat the process a number of times and report the last name you find.
#AActual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Zackary.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: K


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
count=input('Enter count:')
position=input('Enter position:')

#repeat the count
i=0
while i< int(count)+1:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')                    # a list 
    n=0                                # Retrieve all of the anchor tags
    for tag in tags:
         n+=1
         if n==int(position):
            print('Retieving:',url)
            url=tag.get('href', None)                #update URL
            break
         else: 
            continue

    i+=1