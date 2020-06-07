fin = open("input.txt")
fout = open("output.txt","w")
     
a = [int(x) for x in fin.read().split()]
if (a[1]*2 + a[2]*2) > a[0]*2:
    fout.write("NO")
else:
    fout.write("YES")
     
fin.close()
fout.close()
