# Assignment 10.2

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
t_list=list()
for line in handle:
    if line.startswith('From '):
        line.rstrip()
        line=line.split()
        time=line[5]
        t_list.append(time[0:2])
#sort time
for t in t_list:
        counts[t]=counts.get(t,0)+1
list=sorted(counts.items())

#print
for r,v in list:
    print(r,v)
    
