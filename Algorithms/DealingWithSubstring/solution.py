import sys


input_data = sys.stdin.read().split()
n = int(input_data[0])
s = input_data[1]
x = input_data[2]
y = input_data[3]
q = int(input_data[4])
mod = 10**9 + 7
pow2 = [1] * (n + 1)
inv2 = [1] * (n + 1)
InV2 = (mod + 1) // 2
for i in range(1, n + 1):
    pow2[i] = (pow2[i - 1] * 2) % mod
    inv2[i] = (inv2[i - 1] * InV2) % mod
pa = [0] * (n + 1)
pb = [0] * (n + 1)
pba = [0] * (n + 1)
pp = [0] * (n + 1)
for i in range(n):
    ch = s[i]
    a1 = inv2[i + 1] if ch == x else 0
    b1 = pow2[i] if ch == y else 0
    c1 = 1 if (ch == x and x == y) else 0
    pa[i + 1] = (pa[i] + a1) % mod
    pb[i + 1] = (pb[i] + b1) % mod
    pp[i + 1] = pp[i] + c1
    pba[i + 1] = (pba[i] + b1 * pa[i]) % mod
idx = 5
out = []
for _ in range(q):
    l = int(input_data[idx])
    r = int(input_data[idx + 1])
    idx += 2
    t1 = (pba[r + 1] - pba[l]) % mod
    t2 = (pa[l] * (pb[r + 1] - pb[l])) % mod
    res = (t1 - t2 + mod) % mod
    if x == y:
        res = (res + pp[r + 1] - pp[l]) % mod
    out.append(str(res))
sys.stdout.write("\n".join(out) + "\n")