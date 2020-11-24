arr = []
a = list(map(str, input().split()))

for i in a:
    arr.append(str(len(i)))
print(' '.join(arr))
