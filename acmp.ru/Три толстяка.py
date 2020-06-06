import sys
 
a = list(map(int, input().split()))
 
if a[0] > 727 or a[1] > 727 or a[2] > 727:
    print("Error")
    sys.exit()
if a[0] < 94 or a[1] < 94 or a[2] < 94:
    print("Error")
    sys.exit()
 
print(max(a))
