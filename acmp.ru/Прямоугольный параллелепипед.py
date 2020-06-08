fin = open("input.txt")
fout = open("output.txt","w")
     
a = [int(x) for x in fin.read().split()]
v = a[0]*a[1]*a[2]
s = a[0]*a[1]*2 + a[0]*a[2]*2 + a[1]*a[2]*2
fout.write("%s %s" % (s, v))
     
fin.close()
fout.close()
