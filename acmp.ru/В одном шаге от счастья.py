n = int(input())
a = []
for i in range(n):
    a.append(str(input()))
l = 0
r = 0
for i in a:
    l = i[0:3]
    r = i[3:6]
    rp = sum(map(int, str(int(r)+1)))
    rn = sum(map(int, str(int(r)-1)))
    if sum(map(int, str(l))) == rp or sum(map(int, str(l))) == rn:
        print("Yes")
    else:
        print("No")
