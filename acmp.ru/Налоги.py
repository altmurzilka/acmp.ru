n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
  
mx = 0
k = 1
  
for i in range(n):
    if a[i] * b[i] * 0.01 > mx:
        mx = a[i] * b[i]  * 0.01
        k = i+1
print(k)
