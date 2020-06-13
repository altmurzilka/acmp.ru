a = input()
count = 0
for i in a:
  if i == '0' or i == '6' or i == '9':
    count += 1
  elif i == '8':
    count += 2
print(count)

