largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done": break
    try: 
            value=int(num)
    except:
            print('Invalid input')
            continue
    if smallest is None and largest is None:
           smallest=value
           largest=value
    elif value<smallest:
         smallest=value
    elif value>largest: 
             largest=value
print("Maximum is", largest)
print('Minimum is', smallest)
