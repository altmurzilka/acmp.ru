a = list(map(str, input()))
tgl = True
for i in a:
  if i != '1':
    tgl = False
    print("NO")
    break
if tgl:
    print("YES")
    
