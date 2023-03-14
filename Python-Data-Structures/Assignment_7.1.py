# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    f=line.rstrip() // delete end of string by ()
    out=f.upper()
    print(out)
