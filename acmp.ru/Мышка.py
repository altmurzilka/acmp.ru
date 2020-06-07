fin = open("input.txt")
fout = open("output.txt","w")
       
a = [int(x) for x in fin.read().split()]
if a[0] >= a[2]*2 and a[1] >= a[2]*2:
    fout.write("YES")
else: fout.write("NO")
       
fin.close()
fout.close()
