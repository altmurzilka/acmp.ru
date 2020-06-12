import sys
n = int(input())
a = list(map(int, input().split()))
ind = 0
for i in a:
  if i <= 437:
    ind = a.index(i) + 1
    print("Crash " + str(ind))
    sys.exit()
print("No crash")
