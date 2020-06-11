a = int(input())
b = list("{:06d}".format(a))
b = list(map(int, b))
if b[0]+b[1]+b[2] == b[3]+b[4]+b[5]:
  print("YES")
else: print("NO")
