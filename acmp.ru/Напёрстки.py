n = input()
c = 1

for i in range(0, len(n)):
  if n[i] == 'A':
    if c == 1:
      c = 2
    elif c == 2:
      c = 1

  if n[i] == 'B':
    if c == 2:
      c = 3
    elif c == 3:
      c = 2

  if n[i] == 'C':
    if c == 1:
      c = 3
    elif c == 3:
      c = 1

print(c)
