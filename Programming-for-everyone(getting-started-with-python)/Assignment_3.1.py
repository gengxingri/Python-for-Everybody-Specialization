# Assignment 3.1

hrs = input("Enter Hours:")
h = float(hrs)
rate = input('Rate per hour:')
r=float(rate)
if h>40:
    p=40*r+(h-40)*1.5*r 
    print(p) 
else: 
    p=h*r
    print(p)
