a = [int(x) for x in input().split()]
even = -10000
odd = 10000
for i in range(1, len(a), 2):
    if a[i] > even:
        even = a[i]
for j in range(0, len(a), 2):
    if a[j] < odd:
        odd = a[j]
print(even + odd)
