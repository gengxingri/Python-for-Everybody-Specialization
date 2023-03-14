score = input("Enter Score: ")
try:
  sr=float(score)
except:
  print('Error!')
  quit()
if sr>1.0 or sr<0.0:
    re='Error'
elif sr>=0.9:
       re='A'
elif sr>=0.8:
        re='B'
elif sr>=0.7:
        re='C'        
elif sr>=0.6:
        re='D'
elif sr<0.6 and sr>=0.0:
        re='F'  
print(re)
