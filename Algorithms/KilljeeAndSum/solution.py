import sys

input1 = sys.stdin.read().split()
if not input1:
    sys.exit()
mod = 10000019
t = int(input1[0])
idx = 1
qs = []
req = {0}
for _ in range(t):
    n = int(input1[idx])
    m = int(input1[idx + 1])
    r = int(input1[idx + 2])
    idx += 3
    if r < 2:
        qs.append((n, m, r, []))
        continue
    vn, vk = n + m - 2, r - 2
    p = []
    ok = True
    while vn > 0 or vk > 0:
        ni, ki = vn % mod, vk % mod
        if ki > ni:
            ok = False
            break
        if ki > 0 and ni > 0:
            p.append((ni, ki))
            req.update((ni, ki, ni - ki))
        vn //= mod
        vk //= mod
    qs.append((n, m, r, p if ok else None))
sr = sorted(req)
fm = {0: 1}
c = 1
pr = 0
for x in sr:
    if x == 0:
        continue
    for i in range(pr + 1, x + 1):
        c = (c * i) % mod
    fm[x] = c
    pr = x
out = []
for n, m, r, p in qs:
    if r < 2 or p is None:
        out.append("0")
        continue
    res = 1
    for ni, ki in p:
        res = (res * fm[ni] * pow(fm[ki] * fm[ni - ki] % mod, mod - 2, mod)) % mod
    t1 = (n % mod) * (m % mod) % mod * res % mod
    out.append(str(t1))
sys.stdout.write('\n'.join(out) + '\n')