l, w, h = map(int, input().split())
x = (l*h*2 + w*h*2)
if x % 16 != 0: 
  print(x//16+1)
else: print(x//16)
