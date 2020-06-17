n, m = map(int, input().split())

if n == 0 and m > 0:
  print('Impossible')
elif m == 0:
  print("%s %s" % (n, n))
elif n > m:
  print("%s %s" % (n, n+m-1))
else:
  print("%s %s" % (m, n+m-1))
