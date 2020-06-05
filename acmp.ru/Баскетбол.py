fin = open("input.txt")
fout = open("output.txt","w")

a = [int(x) for x in fin.read().split()]
sum1 = 0
sum2 = 0
for i in range(0, len(a), 2):
    sum1 += a[i]

for i in range(1, len(a), 2):
    sum2 += a[i]

if sum1 > sum2:
    fout.write("1")
elif sum1 < sum2:
    fout.write("2")
else: fout.write("DRAW")

fin.close()
fout.close()
