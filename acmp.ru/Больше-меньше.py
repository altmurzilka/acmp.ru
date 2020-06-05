fin  = open("input.txt")
fout = open("output.txt","w")
  
a = [int(x) for x in fin.read().split()]
if a[0] > a[1]:
    fout.write(">")
elif a[0] < a[1]:
    fout.write("<")
else: fout.write("=")

fin.close()
fout.close()
