n, x, y= map(int, input().split())
if x > y:
  temp = x
  x = y
  y = temp
w1 = y - x - 1
w2 = n - y + x - 1
print(min(w1, w2))

