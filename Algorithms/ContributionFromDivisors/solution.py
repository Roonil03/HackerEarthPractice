import sys

input1 = sys.stdin.read().split()
q = [int(v) for v in input1[1:]]
m = max(q)
f = [0] * (m + 1)
for i in range(1, m + 1):
    f[i] = f[i // 10] + (i % 10 if i % 2 else 0)
g = [0] * (m + 1)
for i in range(1, m + 1):
    a = f[i]
    if a:
        for j in range(i, m + 1, i):
            g[j] += a
sys.stdout.write("\n".join(str(g[v]) for v in q) + "\n")