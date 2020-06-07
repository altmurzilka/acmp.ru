fin = open("input.txt")
fout = open("output.txt","w")
    
a = [str(x) for x in fin.read().split()]
a.pop(0)
strng = " "
fout.write("%s" % strng.join(a[::-1]))
    
fin.close()
fout.close()
