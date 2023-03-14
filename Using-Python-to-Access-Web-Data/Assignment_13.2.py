#The program will prompt for a URL, read the JSON data from that URL 
#using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#import json
#Actual data: http://py4e-data.dr-chuck.net/comments_1466065.json

import urllib.request, urllib.parse, urllib.error
import json


#prompt an input
url=input('Enter location: ')
data=urllib.request.urlopen(url).read()

#json type
info = json.loads(data)
sum=0
print('Retrieved:', len(info['comments']))
for item in info['comments']:
    sum+=int(item['count'])
print(sum)
    
    
