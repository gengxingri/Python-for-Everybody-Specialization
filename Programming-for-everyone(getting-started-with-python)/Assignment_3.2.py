def computepay(h, r):
    if h<=40:
        re=h*r
    else: re=h*r+(h-40)*0.5*r
    return re

hrs = input("Enter Hours:")
rate = input('Rate per hour:')
h=float(hrs)
r=float(rate)
p = computepay(h, r)
print("Pay", p)
