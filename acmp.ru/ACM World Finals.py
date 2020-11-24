t = input()
p1 = input()
p2 = input()
p3 = input()

arr = []
arr.append(p1)
arr.append(p2)
arr.append(p3)

arr.sort()

print("%s: %s, %s, %s" % (t, arr[0], arr[1], arr[2]))
