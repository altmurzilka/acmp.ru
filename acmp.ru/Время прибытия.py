n = input().split(':')
h, m = list(map(int, input().split()))
x = int(n[0]) + h
y = int(n[1]) + m
x += y//60
y = y%60
x = x%24
print("{:02d}:{:02d}".format(x, y))
