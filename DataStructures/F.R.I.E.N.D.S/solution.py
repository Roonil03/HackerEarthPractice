import sys

input1 = sys.stdin.read().split()
idx = 0
t = int(input1[idx])
idx += 1
for _ in range(t):
    n = int(input1[idx])
    idx += 1
    X = [0] * (n + 1)
    Y = [0] * (n + 1)
    adds = [[] for _ in range(n + 2)]
    rems = [[] for _ in range(n + 2)]
    for i in range(1, n + 1):
        X[i] = int(input1[idx])
        Y[i] = int(input1[idx + 1])
        idx += 2
        L = i + 1 if i + 1 > X[i] else X[i]
        R = Y[i]
        if L <= R and L <= n:
            adds[L].append(i)
            if R + 1 <= n:
                rems[R + 1].append(i)
    bit = [0] * (n + 1)
    ans = 0
    for j in range(1, n + 1):
        for i in adds[j]:
            while i <= n:
                bit[i] += 1
                i += i & (-i)
        for i in rems[j]:
            while i <= n:
                bit[i] -= 1
                i += i & (-i)
        q_L = X[j]
        q_R = j - 1 if j - 1 < Y[j] else Y[j]
        if q_L <= q_R:
            s = 0
            while q_R > 0:
                s += bit[q_R]
                q_R -= q_R & (-q_R)
            q_L -= 1
            while q_L > 0:
                s -= bit[q_L]
                q_L -= q_L & (-q_L)
            ans += s
    print(ans)