import sys 
import bisect

input1 = sys.stdin.read().split()
n = int(input1[0])
q = int(input1[1])
a = [0] * (2 * n)
for i in range(n):
    a[i] = int(input1[2 + i])
for i in range(n, 2 * n):
    a[i] = a[i - n]
v = {}
for i in range(2 * n):
    if a[i] not in v:
        v[a[i]] = []
    v[a[i]].append(i)
query_idx = 2 + n
out = []
for _ in range(q):
    m = 200000
    x = int(input1[query_idx])
    y = int(input1[query_idx + 1])
    query_idx += 2
    if x in v and y in v:
        vx = v[x]
        vy = v[y]
        for pos_x in vx:
            h = bisect.bisect_right(vy, pos_x)
            if h < len(vy):
                m = min(m, abs(vy[h] - pos_x))
            if h != 0:
                m = min(m, abs(pos_x - vy[h - 1]))
    out.append(m // 2)
sys.stdout.write("\n".join(map(str, out)) + "\n")