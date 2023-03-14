import re 
digits=list()
fh=open('regex_sum_1466060.txt')
for line in fh:
	line.rstrip()
	num=re.findall('[0-9]+',line)
	digits=digits+num
length=len(digits)
print(length)
for i in range(length):
	digits[i]=int(digits[i])
print(sum(digits))
   


