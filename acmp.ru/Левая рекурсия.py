a = int(input())

count = 0
arr = []
for i in range(0, a):
    k = input()
    arr.append(k)

garr =[]
for i in arr:
    for j in i:
        if i.index(j) == 0: 
            garr.append(j)
        if i.index(j) == 3:
            garr.append(j)
    if garr[0] == garr[1]:
        count += 1
    garr.clear()

print(count)
