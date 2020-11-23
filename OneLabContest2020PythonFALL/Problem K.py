a = list(map(int, input().split()))
arr = []
for n in sorted(a):
    if ((n & (n-1) == 0) and n != 0):
        arr.append(n)
    
for i in sorted(set(arr)):
    print(i, end=" ")
