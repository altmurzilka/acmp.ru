n, a1, a2 = map(int, input().split())
 
a0 = 0
for i in range(0, n-1):
    a0 = a2 - a1
    a2 = a1
    a1 = a0
 
print(a1, a2)
