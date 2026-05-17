import sys

data = sys.stdin.read().split()
n, a, mod = int(data[0]), int(data[1]), int(data[2])
pow = [1 % mod] * (n + 1)
for i in range(1, n + 1):
    pow[i] = (pow[i - 1] * a) % mod
res = 0
for k in range(1, n):
    m = n - k
    par = list(range(n))
    comps = n
    ks = 0
    def dfs(id, sign):
        global comps, ks
        if id > m:
            ks += sign * pow[comps]
            return
        dfs(id + 1, sign)
        sed = []
        for j in range(k):
            u = j
            while u != par[u]: u = par[u]
            v = id + j
            while v != par[v]: v = par[v]
            if u != v:
                par[u] = v
                comps -= 1
                sed.append(u)
        dfs(id + 1, -sign)
        for u in sed:
            par[u] = u
            comps += 1
    dfs(1, -1)
    res = (res + ks + pow[n]) % mod
print(res)
