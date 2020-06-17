import sys
s, p = map(int, input().split())

for i in range(1, max(s, p)):
  for j in range(1, min(s,p)):
    if i+j == s and i*j == p:
      print(i, j)
      sys.exit()
