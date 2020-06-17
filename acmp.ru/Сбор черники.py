n = int(input())
a = list(map(int, input().split()))
 
count = 0
a.append(a[0])
a.append(a[1])
 
temp = 0
for i in range(1, n+1):
    temp = a[i-1] + a[i] + a[i+1]
    if temp > count:
        count = temp
 
print(count)
