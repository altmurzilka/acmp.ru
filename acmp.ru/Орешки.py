fin = open("input.txt")
fout = open("output.txt","w")
   
a = [int(x) for x in fin.read().split()]
   
for i in a:
  if a[0]*a[1] >= a[2]:
    fout.write("YES")
    break
  else: 
    fout.write("NO")
    break
   
fin.close()
fout.close()
