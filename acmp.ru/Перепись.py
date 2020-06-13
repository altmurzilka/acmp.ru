n = int(input())
max = 0
k = -1
for i in range(0, n):
  a, s = map(int, input().split())
  if s == 1 and a > max:
    max = a
    k = i+1
print(k)
