import sys

input1 = sys.stdin.read().split()
p1, p2, k = map(int, input1)
mod = 10**9+7
if p1 + p2 == 0:
    print(0)
else:
    res = (pow(10, k, mod) - pow((10 - p1 - p2) % mod, k, mod)) % mod
    res = (res * p1 * pow(p1+p2, mod - 2, mod)) % mod
    print(res)