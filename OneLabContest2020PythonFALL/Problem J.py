from math import sqrt
from itertools import count, islice

a, b = map(int, input().split())

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

arr = []
for i in range(a, b):
    if is_prime(i):
        arr.append(i)
    
  
arr = sorted(arr, key=int, reverse=True)
str1 = ' '.join(str(e) for e in arr)
print(str1)
