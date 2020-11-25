from collections import Counter

n = int(input())
a = list(map(int, input().split()))
f = Counter(a)
arr = []
for k, v in f.items():
    if v == max(f.values()):
        arr.append(k)
if len(arr) > 1:
    print(0)
else: 
    print(arr[0])
