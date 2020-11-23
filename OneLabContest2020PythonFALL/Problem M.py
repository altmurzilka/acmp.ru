string=input()
f={}
for i in string:
  f[i]=f.get(i,0)+1
print(len(f.keys()))

for i in sorted(f):
    print(i, f[i])
