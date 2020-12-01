a, b = map(int, input().split())

d = []
for i in range(0, a):
    k = input()
    d.append(k)

arr = []
for i in d:
    count = 0
    for j in range(b):
        if i[j] == '.':
            count += 1
    arr.append(count)
print(min(arr))