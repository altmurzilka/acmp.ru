fin  = open("input.txt")
fout = open("output.txt","w")
  
x = [i.split() for i in fin]
flatList = [item for sublist in x for item in sublist]
if (int(flatList[0]) < 1 or int(flatList[0]) > 100):
    exit()
else:
    del flatList[0]
    even_arr = []
    odd_arr = []
    for i in flatList:
        if int(i) > 31 or int(i) < 1:
            exit()
    for i in flatList:
        if int(i)%2 == 0:
            even_arr.append(i)
        else:
            odd_arr.append(i)
    str_even = ' '.join(even_arr)
    str_odd = ' '.join(odd_arr)
     
    fout.write(str_odd)
    fout.write('\n')
    fout.write(str_even)
    fout.write('\n')
    if len(even_arr) >= len(odd_arr):
        fout.write('YES')
    else: fout.write('NO')
      
fin.close()
fout.close()
