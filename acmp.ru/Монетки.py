fin = open("input.txt")
fout = open("output.txt","w")
   
a = [int(x) for x in fin.read().split()]
a.pop(0)
  
sum0 = 0
sum1 = 0
  
for i in a:
  if i == 1:
    sum1 += 1
  else: sum0 += 1
  
if sum1 > sum0 or sum1 == sum0: 
  fout.write(str(sum0))
else: fout.write(str(sum1))
   
fin.close()
fout.close()
