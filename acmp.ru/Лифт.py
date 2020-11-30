b = input()
count = 0
maximum = 0
minimum = 0
for i in b:
    if i == '1':
        count += 1
    else: 
        count -= 1
    if count > maximum:
        maximum = count
    if count < minimum:
        minimum = count
print(maximum - minimum + 1)
