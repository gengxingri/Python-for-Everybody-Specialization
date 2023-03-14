fname = input("Enter file name: ")
fh = open(fname)


lis=list()
for line in fh:
    line=line.rstrip()
    x=line.split()
    #check the words 
    for  word in x:
       if word not in lis:
          lis.append(word) 
lis.sort()
print(lis)

#words_list=[]
#for line in fh:
 #   words=line.rstrip().split(' ')
  #  for word in words:
   #     if word not in words_list:
    #    words_list.append(word)
#print(sorted(words_list))    
#print(sorted(list(set(words_list))))
    
    
