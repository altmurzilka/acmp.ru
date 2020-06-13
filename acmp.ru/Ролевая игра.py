n, m, k = map(int, input().split())
print(int((m//k + min(k-1, m))*n))
