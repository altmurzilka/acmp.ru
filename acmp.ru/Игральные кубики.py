n = int(input())
max = n*6
min = n//6
n %= 6
if n%6 > 0:
  min += 7-n
print(min, max)
