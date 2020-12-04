n = int(input())
k = list(map(int, input().split()))

narr = []
parr = []
a = []
b = []

for i in range(n):
    if k[i] > 0:
        a.append(str(i + 1))
        parr.append(k[i])
    if k[i] < 0:
        b.append(str(i + 1))
        narr.append(k[i])

if abs(sum(narr)) >= sum(parr):
    print(len(narr))
    print(" ".join(b))
elif abs(sum(narr)) < sum(parr):
    print(len(parr))
    print(" ".join(a))
