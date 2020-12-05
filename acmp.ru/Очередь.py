n = int(input())

if n > 145:
    print("NO")
else:
    t = n*5 - 5
    print(t//60, t%60)
