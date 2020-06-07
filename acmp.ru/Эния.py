fin = open("input.txt")
fout = open("output.txt","w")
    
a = [int(x) for x in fin.read().split()]
mul = 1
 
for i in a:
  mul = mul * i
fout.write(str(mul*2))
    
fin.close()
fout.close()
