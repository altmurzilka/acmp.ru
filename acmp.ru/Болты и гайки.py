b = list(map(int, input().split()))
g = list(map(int, input().split()))
 
sum = 0
sum1 = 0
sum2 = 0
 
sum1 = (b[0]*b[1])/100
sum2 = (g[0]*g[1])/100
 
b[0] -= sum1
g[0] -= sum2
 
sum = sum1*b[2] + sum2*g[2]
 
if b[0] > g[0]:
    sum += (b[0] - g[0])* b[2]
else:
    sum += (g[0] - b[0])* g[2]
     
print(int(sum))
