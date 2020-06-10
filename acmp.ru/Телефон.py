a, b, c, t = map(int, input().split())
if (t - a) > 0:
  print(a*b + (t-a)*c)
elif (t - a) < 0:
  print(t*b)
else: print(a*b)
