

#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts 
#from the XML data, compute the sum of the numbers in the file.
#Actual data: http://py4e-data.dr-chuck.net/comments_1466064.xml






import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url=input('Enter location: ')
uh = urllib.request.urlopen(url).read()
       
#get the tree of XML
tree=ET.fromstring(uh) 

#get a list of strings (in this case: digits)
tags=tree.findall('.//count')

count=0
sum=0
for tag in tags:
     count+=1
     sum+= int(tag.text)
print(count,sum)

    
  


   
