import sys

input1 = sys.stdin.read().split()
n, k = int(input1[0]), int(input1[1])
p = [0] * (n + 1)
for i in range(n):
    p[i + 1] = p[i] ^ int(input1[i + 2])
MAX = (n + 1) * 20 + 2
n0 = [0] * MAX
n1 = [0] * MAX
count = [0] * MAX
tot = 1
for v in p:
    u = 0
    count[u] += 1
    for i in range(19, -1, -1):
        if(v >> i) & 1:
            if not n1[u]:
                n1[u] = tot
                tot += 1
            u = n1[u]
        else:
            if not n0[u]:
                n0[u] = tot
                tot += 1
            u = n0[u]
        count[u] += 1
nodes = [0] * (n + 1)
res = 0
for i in range(19, -1, -1):
    c = 0
    for j in range(n + 1):
        u = nodes[j]
        if u != -1:
            child = n0[u] if ((p[j] >> i) & 1) else n1[u]
            if child:
                c += count[child]
    c //= 2
    if c >= k:
        res |= (1 << i)
        for j in range(n + 1):
            u = nodes[j]
            if u != -1:
                child = n0[u] if ((p[j] >> i) & 1) else n1[u]
                nodes[j] = child if child else -1
    else:
        k -= c
        for j in range(n + 1):
            u = nodes[j]
            if u != -1:
                child = n1[u] if ((p[j] >> i) & 1) else n0[u]
                nodes[j] = child if child else -1
print(res)