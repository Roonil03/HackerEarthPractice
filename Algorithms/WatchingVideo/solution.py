import sys

input1 = sys.stdin.read().split()
n = int(input1[0])
d = int(input1[1])
res = 0
p = 0
for t in range(1, n + 1):
    c = p + int(input1[t + 1])
    if c // d > p // d:
        res = max(res, t - (p // d))
    p = c
print(res)