n1, p1 = map(int, input().split())
n2, p2 = map(int, input().split())


def number_sum(n, p):
    count = 0
    while n > 0:
        count += n%p
        n = n//p
    return count

if number_sum(n1, p1) == number_sum(n2, p2):
    print(number_sum(n1, p1))
else:
    print(0)
