import sys

input = sys.stdin.read
data = input().split()
idx = 0
t = int(data[idx])
idx += 1
out = []
for _ in range(t):
    x = int(data[idx])
    y = int(data[idx + 1])
    n = int(data[idx + 2])
    idx += 3
    m = []
    for _ in range(n):
        m.append(int(data[idx]))
        idx += 1
    dp = [[0] * n for _ in range(n)]
    for l in range(2, n):
        for i in range(n - l):
            j = i + l
            temp = float("inf")
            for k in range(i + 1, j):
                cost = (
                    dp[i][k] + dp[k][j]
                    + x * (m[k] - m[i])
                    + y * (m[j] - m[k])
                )
                if cost < temp:
                    temp = cost
            dp[i][j] = temp
    out.append(str(dp[0][n-1]))
print("\n".join(out))