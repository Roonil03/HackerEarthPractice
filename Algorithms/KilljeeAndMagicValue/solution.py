import sys

input1 = sys.stdin.read().split()[1:]
r = []
for i in range(0, len(input1), 3):
    n, m, k = int(input1[i]), int(input1[i + 1]), int(input1[i + 2])
    mod = k * 1000000007
    res, a, b, f = 0, 1, 1, 1
    # for j in range(1, n):
    #     f = f * i % m
    #     a, b = b, a + b
    #     if b >= m:
    #         b -= m
    # for j in range(n, m + 1):
    #     f = f * i % m
    #     res = (res + b * f) % m
    #     a, b = b, a + b
    #     if b >= m:
    #         b -= m
    for j in range(1, m + 1):
        f = (f * j) % mod
        if j >= n:
            res = (res + b * f) % mod
        a, b = b, a + b
        if b >= mod:
            b -= mod
    r.append(str(res // k))
sys.stdout.write('\n'.join(r) + '\n')