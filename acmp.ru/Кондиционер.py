s, t = map(int, input().split())
temp = input()
if temp == 'heat': 
  print(max(t, s))
elif temp == 'freeze': 
  print(min(t, s))
elif temp == 'auto':
  print(t)
elif temp == 'fan': 
  print(s)
