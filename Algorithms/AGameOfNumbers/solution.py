import sys

input1 = sys.stdin.read().split()
n = int(input1[0])
a = [int(x) for x in input1[1:n + 1]]
f = [-1] * n
g = [-1] * n
s1, s2 = [], []
for i in range(n):
    while s1 and a[s1[-1]] < a[i]:
        f[s1.pop()] = i
    s1.append(i)
    while s2 and a[s2[-1]] > a[i]:
        g[s2.pop()] = i
    s2.append(i)
res = [str(a[g[f[i]]]) if f[i] != -1 and g[f[i]] != -1 else "-1" for i in range(n)]
sys.stdout.write(" ".join(res) + "\n")