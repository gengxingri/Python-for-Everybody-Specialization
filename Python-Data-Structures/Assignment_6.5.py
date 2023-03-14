# Assignment 6.5

text = "X-DSPAM-Confidence:    0.8475"
pos=text.find('0')
x=text[pos:]
num=float(x)
print(x)
