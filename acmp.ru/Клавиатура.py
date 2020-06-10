letter = input()
qwerty = 'qwertyuiopasdfghjklzxcvbnm'
lower = letter.lower()
for i in qwerty:
  if lower == 'm':
    print('q')
    break
  elif i == lower:
    print(qwerty[qwerty.index(i)+1])
