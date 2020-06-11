p, s = map(int, input().split())
  
if s%p != 0:
    print((s//p)+1, s%p)
elif s%p == 0:
    print(s//p, p)
else: print(s//p, s%p)
