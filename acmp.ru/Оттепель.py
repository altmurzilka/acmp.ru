n = int(input())
a = list(map(int, input().split()))
ind = 0
mxm = 0
for i in a:
    if i > 0:
        ind += 1
    else: ind = 0
    if ind>mxm:
        mxm = ind
print(mxm)
