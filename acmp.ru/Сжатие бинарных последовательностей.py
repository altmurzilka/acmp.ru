n = input()
count = 0
s = ''
for i in n:
    if i == '0':
        count += 1
    else:
        s += chr(ord('a')+count)
        count = 0
print(s)
