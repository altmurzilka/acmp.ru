t = list(input())

arr = []

for i in t:
    if i == 'A':
        arr.append('T')
    elif i == 'G':
        arr.append('C')
    elif i == 'C':
        arr.append('G')
    elif i == 'T':
        arr.append('A')
print(''.join(arr))

