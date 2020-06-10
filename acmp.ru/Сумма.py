fin  = open("input.txt")
fout = open("output.txt","w")
  
x = int(fin.readline().strip())
cnt = 0
if x > 0:
    for i in range(1, x+1):
        cnt = cnt+i
else:
    for i in range(x, 2):
        cnt = cnt+i
fout.write(str(cnt))
  
fin.close()
fout.close()
