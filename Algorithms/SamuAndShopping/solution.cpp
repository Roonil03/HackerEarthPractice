import sys

input = sys.stdin.read
data = input().split()
idx = 0
t = int(data[idx])
idx += 1
out = []
for _ in range(t):
    n = int(data[idx])
    idx += 1
    dp0 = int(data[idx])
    dp1 = int(data[idx + 1])
    dp2 = int(data[idx + 2])
    idx += 3
    for _ in range(1, n):
        c0 = int(data[idx])
        c1 = int(data[idx + 1])
        c2 = int(data[idx + 2])
        idx += 3
        ndp0 = c0 + (dp1 if dp1 < dp2 else dp2)
        ndp1 = c1 + (dp0 if dp0 < dp2 else dp2)
        ndp2 = c2 + (dp0 if dp0 < dp1 else dp1)
        dp0, dp1, dp2 = ndp0, ndp1, ndp2
    res = min(dp0, min(dp1, dp2))
    out.append(str(res))
print("\n".join(out))