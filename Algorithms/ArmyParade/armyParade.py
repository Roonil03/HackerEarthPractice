import sys

data = sys.stdin.read().split()
n, m, k = map(int, data[:3])
mod = 2000000033
if n > m:
    n, m = m, n
num, den = 1, 1
for i in range(1, n):
    num = (num * (m - 1 + i)) % mod
    den = (den * i) % mod
comb = (num * pow(den, -1, mod)) % mod
res = ((n * m - k) % mod * comb) % mod
print(res)
