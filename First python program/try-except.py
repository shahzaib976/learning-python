n = 10

# n1 = n/0
# print('n1: ', n1)

try:
    n1 = n/0
    print('n1: ', n1)
except:
  print("Division by zero is not allowed")
else:
  print("Nothing went wrong")
finally:
   print('Im finished')
   


l = [1]
try:
   print(l[0])
except:
   print('Invalid list index provided')
finally:
   print('Im finished')
