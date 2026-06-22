import sys

input1 = sys.stdin.read().split()
t = int(input1[0])
mod = 1000000007
res = []
for i in range(1, t+1):
    n = int(input1[i])
    res.append(str((pow(2, n, mod) - 2) % mod))
print('\n'.join(res))