n = int(input())

d = {}
for i in range(0, n):
    a, b = map(int, input().split())
    d.update({a:b})

mn = 32
mx = 0
for k, v in d.items():
    if k > mx:
        mx = k
    if v < mn:
        mn = v

if mn - mx >= 0:
    print("YES")
else: 
    print("NO")
