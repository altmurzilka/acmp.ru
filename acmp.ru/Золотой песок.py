fin = open("input.txt")
fout = open("output.txt","w")
     
a = [int(x) for x in fin.read().split()]
listA = []
listB = []

for i in range(0, 3):
    listA.append(a[i])
for i in range(0, 3):
    a.pop(0)
listB = a

listA = sorted(listA)
listB = sorted(listB)

fout.write(str(listA[0]*listB[0] + listA[1]*listB[1] + listA[2]*listB[2]))
     
fin.close()
fout.close()
