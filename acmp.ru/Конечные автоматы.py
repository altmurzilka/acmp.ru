fin = open("input.txt")
fout = open("output.txt","w")

a = [int(x) for x in fin.read().split()]
a.pop(0)

for i in range(0, len(a), 2):
    chunk = a[i:i+2]
    m, n = map(int, chunk)
    d = int(19*n + ((m + 239)*(m + 366)/2))
    fout.write("%s\n" % d) 

fin.close()
fout.close()
