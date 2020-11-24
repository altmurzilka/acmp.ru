n = int(input())
a = list(map(int, input().split()))
count = 0
avg = 0
for i in range(0, len(a), 2):
    if a[i]%2 == 0:
        avg += 1
        count += a[i]
if avg == 0:
    print(0)
else: print("{:.6f}".format(count/avg))
