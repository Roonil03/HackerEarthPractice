import sys

input1 = sys.stdin.read().split()
n, k = int(input1[0]), int(input1[1])
s = list(input1[2])
par = list(range(n + 2))
size = [0] * (n + 2)
def find(i):
    cur = i
    while par[cur] != cur:
        cur = par[cur]
    while i != cur:
        nxt = par[i]
        par[i] = cur
        i = nxt
    return cur
def union(i, j):
    ri, rj = find(i), find(j)
    if ri != rj:
        par[ri] = rj
        size[rj] += size[ri]
temp = 0
for i in range(1, n + 1):
    if s[i - 1] == '1':
        size[i] = 1
        temp = max(temp, 1)
        if i > 1 and s[i - 2] == '1':
            union(i, i - 1)
            temp = max(temp, size[find(i)])
idx = 3
res = []
for _ in range(k):
    if input1[idx] == '1':
        res.append(str(temp))
        idx += 1
    else:
        x = int(input1[idx + 1])
        idx += 2
        if s[x - 1] == '0':
            s[x - 1] = '1'
            size[x] = 1
            temp = max(temp, 1)
            if x > 1 and s[x - 2] == '1':
                union(x, x - 1)
            if x < n and s[x] == '1':
                union(x, x + 1)
            temp = max(temp, size[find(x)])
if res:
    sys.stdout.write('\n'.join(res) + '\n')