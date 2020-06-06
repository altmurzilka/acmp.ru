fin = open("input.txt")
fout = open("output.txt","w")
       
a = [int(x) for x in fin.read().split()]
fout.write(str(a[0]+(a[2]-1)*(a[1]-a[0])))
       
fin.close()
fout.close()
