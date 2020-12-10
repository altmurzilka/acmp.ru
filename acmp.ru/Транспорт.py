n, v, l = map(int, input().split())
if n == 0:
    print(format(l/v*60, '.2f'))
else:
    ft = l / v * 60
    a = list(map(int, input().split())) 
    for i in range(len(a)):
        if i%2 != 0:
            ft += a[i]
    print(format(ft, '.2f'))
