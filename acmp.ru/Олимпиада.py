fin = open("input.txt")
fout = open("output.txt","w")

a = [int(x) for x in fin.read().split()]
a.pop(0)

sum5 = 0
sum3 = 0
sum1 = 0

for i in range(0, len(a)):
    sum5 += sum5 + a[i]
sum5 = sum5 - a[0]

a3 = a[::-1]
for i in range(0, len(a3)):
    sum3 += sum3 + a3[i]
sum3 = sum3 - a3[0]

a1 = sorted(a)
for i in range(0, len(a1)):
    sum1 += sum1 + a1[i]
sum1 = sum1 - a1[0]

if sum1 < sum3 and sum1 < sum5:
    fout.write("1")
elif sum3 < sum1 and sum3 < sum5:
    fout.write("3")
elif sum1 == sum3 or sum1 == sum5:
    fout.write("1")
elif sum3 == sum5:
    fout.write("3")
elif sum5 < sum1 and sum5 < sum3:
    fout.write("5")

fin.close()
fout.close()
