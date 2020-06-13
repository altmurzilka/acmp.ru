n = int(input())
arr = [int(i) for i in input().split()]
m = int(input())
marr = [[int(j) for j in input().split()] for i in range(m)]
   
for i in range(m):
  for j in range(marr[i][0]-1, marr[i][1]):
    print("%s " % arr[j])
  print()
