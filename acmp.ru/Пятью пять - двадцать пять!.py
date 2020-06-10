fin  = open("input.txt")
fout = open("output.txt","w")
  
x = int(fin.readline().strip())
if x%5 == 0:
    fout.write(str(x**2))
  
fin.close()
fout.close()
