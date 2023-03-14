# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
tot=0
#iteration 
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    pos=line.find('0')
    x=line[pos:]
    num=float(x)
    tot=tot+num
    ave=tot/count
print("Average spam confidence:", ave)
