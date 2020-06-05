fin  = open("input.txt")
fout = open("output.txt","w")
  
a = [int(x) for x in fin.read().split()]
fout.write(str(max(a) - min(a)))

fin.close()
fout.close()
