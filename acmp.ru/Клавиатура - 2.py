n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))

arr = []
for i in range(1, n+1):
    arr.append(p.count(i))

garr = []
for i in range(n):
    garr.append(c[i] - arr[i])

for i in garr:
    if i<0:
        print('yes')
    else: 
        print('no')
