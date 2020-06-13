import math

a, b = map(int, input().split())
number = a*b
root = math.sqrt(number)
print(int(root) if int(root + 0.5) ** 2 == number else 0)
