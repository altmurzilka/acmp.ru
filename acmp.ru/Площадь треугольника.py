from math import sqrt

x1, y1, x2, y2, x3, y3 = map(int, input().split())

a = sqrt((x2-x1)**2 + (y2-y1)**2)
b = sqrt((x3-x2)**2 + (y3-y2)**2)
c = sqrt((x1-x3)**2 + (y1-y3)**2)

p = (a + b + c)/2

print('{:.1f}'.format(sqrt(p*(p-a)*(p-b)*(p-c))))
