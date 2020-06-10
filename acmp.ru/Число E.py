e = '2.71828182845904523536028750'
x = int(input())
 
if x <= 0:
    print(3)
else:
    r = e[:x+2]
    if e[x] != '.' and int(e[x+2]) >= 5:
        r = r[:-1] + str(int(e[x+1]) + 1)
        print(r)
    else:
        print(r)
