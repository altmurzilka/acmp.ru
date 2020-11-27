k = int(input())
n, a, b, c = map(int, input().split())
 
if k == 1:
    print(max(a + b + c - 2*n, 0))
else:
    print(min(a, min(b, c)))
