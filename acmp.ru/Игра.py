fin  = open("input.txt")
fout = open("output.txt","w")
  
x = int(fin.readline().strip())
fout.write(str(x)+'9'+str(9-x))
  
fin.close()
fout.close()
