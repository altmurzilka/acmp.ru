fin  = open("input.txt")
fout = open("output.txt","w")
  
x = int(fin.readline().strip())
if (x < 1 or x > 10**9):
    exit()
else:
    fout.write(str(x+1))
      
fin.close()
fout.close()
