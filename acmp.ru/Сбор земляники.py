fin = open("input.txt")
fout = open("output.txt","w")

a = [int(x) for x in fin.read().split()]

if a[2] > (a[0] + a[1]):
    fout.write("Impossible")
else: fout.write(str(a[0] + a[1] - a[2]))

fin.close()
fout.close()
