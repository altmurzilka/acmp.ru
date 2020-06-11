a, b = map(int, input().split())
c = a
while(a%b>0):
    a+=c
print(a)
