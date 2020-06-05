fin = open("input.txt")
fout = open("output.txt","w")

a = [int(x) for x in fin.read().split()]
sum = a[0] + a[1] - 1
fout.write("%s %s" % (sum - a[0], sum - a[1])) 

fin.close()
fout.close()
