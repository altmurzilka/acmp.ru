fin  = open("input.txt")
fout = open("output.txt","w")
   
a, b = map(int, fin.readline().split())
fout.write(str(a*a*b))
   
fin.close()
fout.close()
