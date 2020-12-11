from decimal import *
a = input()
b = input()
if Decimal(a) > Decimal(b):
    print(">")
elif Decimal(a) < Decimal(b):
    print("<")
else:
    print("=")
