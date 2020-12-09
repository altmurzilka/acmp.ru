a, b = map(int, input().split())
  
d = []
for i in range(0, a):
    d.append(input())
 
k = []
for i in range(0, a+1):
    k.append(input())
k.pop(0)
 
count = 0
for i in range(a):
    for j in range(b):
        if d[i][j] == k[i][j]:
            count += 1
 
print(count)
