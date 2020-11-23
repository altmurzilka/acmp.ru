n = int(input())
count = 0
for i in list(bin(n)):
    if i == '1':
        count += 1
print(count+n)
