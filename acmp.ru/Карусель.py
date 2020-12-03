n = int(input())
c = list(map(int, input().split()))

p = 3
count = 0
for i in c:
    if i:
        count += p
        p += 1
    else: 
        p = max(p-3, 3)

print(count)
