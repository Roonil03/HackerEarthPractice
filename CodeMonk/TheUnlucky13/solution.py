import sys

input = sys.stdin.read().split()
t = int(input[0])
q = [int(x) for x in input[1 : t + 1]]
MOD = 1000000009
p = []
a, b, c, d = 9, 8, 1, 1
for _ in range(32):
    p.append((a, b, c, d))
    a, b, c, d = (
        (a * a + b * c) % MOD,
        (a * b + b * d) % MOD,
        (c * a + d * c) % MOD,
        (c * b + d * d) % MOD,
    )
out = []
for n in q:
    x, y = 1, 0
    j = 0
    while n > 0:
        if n & 1:
            ma, mb, mc, md = p[j]
            x, y = (ma * x + mb * y) % MOD, (mc * x + md * y) % MOD
        n >>= 1
        j += 1
    out.append(str((x + y) % MOD))
sys.stdout.write("\n".join(out) + "\n")