import sys

input1 = sys.stdin.read().split()
n = int(input1[0])
arr = [int(x) for x in input1[1:n+1]]
m = max(arr) + 1 if arr else 1
mb = [0] * m
if m > 1:
    mb[1] = 1
for i in range(1, m):
    if mb[i]:
        for j in range(i * 2, m, i):
            mb[j] -= mb[i]
dv = [[] for _ in range(m)]
for i in range(2, m):
    if mb[i]:
        for j in range(i, m, i):
            dv[j].append(i)
s = [0] * m
res = 0
for i, v in enumerate(arr, 1):
    w = n - i + 1
    for x in dv[v]:
        s[x] += i
        res -= mb[x] * s[x] * w
print(1 if res > 10**18 else res)