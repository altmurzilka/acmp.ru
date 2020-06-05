fin  = open("input.txt")
fout = open("output.txt","w")
  
x = int(fin.readline().strip())
if (x < 1 or x > 100):
    exit()
else:
    fout.write(str(x))
      
fin.close()
fout.close()
