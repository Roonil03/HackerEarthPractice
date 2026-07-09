import sys

input1 = sys.stdin.read().split()
out = []
for s in input1[1:]:
    n = int(s)
    p = (4 * n // 5) * 5
    c, t = 0, p
    while t > 0:
        t //= 5
        c += t
    while c < n:
        p += 5
        t = p
        while t % 5 == 0:
            c += 1
            t //= 5
    out.append(str(p))
sys.stdout.write("\n".join(out) + "\n")