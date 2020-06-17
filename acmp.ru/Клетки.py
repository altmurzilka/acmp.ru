a = input()
letters = 'ABCDEFGH'
arr = []
for i in a:
  arr.append(i)
 
lrr = []
for i in letters:
    lrr.append(i)
 
 
for i in lrr:
    if i == arr[0]:
        if (lrr.index(i) + 1 + int(arr[1]))%2 == 0:
            print('BLACK')
        else:
            print('WHITE')
