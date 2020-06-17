n = int(input())
a = list(map(int, input().split()))
r = int(input())
  
sum = 0
for i in a:
  sum += min(r, i)
    
print(sum)
