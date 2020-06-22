fin  = open("input.txt")
fout = open("output.txt","w")
   
x = [i.split() for i in fin]
x.pop(0)
 
name = []
score =[]
 
for i in range(0, len(x), 2):
    name.append(x[i])
 
for i in range(1, len(x), 2):
    score.append(x[i])
 
count = 0
vin = 100001
ndx = 0
for i in score:
    for j in i:
        count += int(j)
    if count < vin:
        vin = count
        ndx = score.index(i)
    count = 0
 
fout.write(''.join(name[ndx]))
       
fin.close()
fout.close()
