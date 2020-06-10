x = int(input())
if (x%400 == 0 or (x%4 == 0 and x%100 != 0)):
  print("12/09/{:04d}".format(x))
else: 
  print("13/09/{:04d}".format(x))
