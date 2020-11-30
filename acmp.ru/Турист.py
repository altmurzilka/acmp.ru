k, w = map(int, input().split())
a1, b1, a2, b2, a3, b3 = map(int, input().split())
  
def is_suits(a, b, k, w):
    return (b>=k and a <= w)

if (is_suits(a1, b1, k, w) or is_suits(a2, b2, k, w) or is_suits(a3, b3, k, w) \
    or is_suits(a1+a2, b1+b2, k, w) or is_suits(a1+a3, b1+b3, k, w) \
        or is_suits(a3+a2, b3+b2, k, w) or is_suits(a1+a2+a3, b1+b2+b3, k, w)):
        print("YES")
else: 
    print("NO")
