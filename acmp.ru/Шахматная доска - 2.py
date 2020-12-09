n, m, i, j, c = map(int, input().split())

if n*m % 2 == 0:
    print("equal")
elif ((i + j) % 2 == c):
    print("black")
else:
    print("white")  
