fin  = open("input.txt")
fout = open("output.txt","w")
  
n, w = map(str, fin.readline().split())
w = list(w)
w.pop(int(n)-1)
fout.write(''.join(map(str, w)))
  
fin.close()
fout.close()
