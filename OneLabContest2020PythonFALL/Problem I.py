string=input()
f={}

for i in string.split():
  f[i]=f.get(i,0)+1

for i in sorted(f):
    print(i, f[i])
