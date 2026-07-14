import sys
from collections import deque

input1 = sys.stdin.read().split()
N, M, a, b, x, y = map(int, input1[:6])
H = [int(v) for v in input1[6:6+N]]
P0 = [0] * (N + 1)
PM = [0] * (N + 1)
for i in range(1, N + 1):
    P0[i] = P0[i-1] + H[i-1] * y
    PM[i] = PM[i-1] + (M - H[i-1]) * x
C0 = [float('inf')] * (N + 1)
CM = [float('inf')] * (N + 1)
C0[0] = CM[0] = 0
dq0 = deque()
dqM = deque()
for i in range(1, N + 1):
    j = i - a
    if j >= 0:
        if C0[j] != float('inf'):
            v0 = C0[j] - PM[j]
            while dq0 and C0[dq0[-1]] - PM[dq0[-1]] >= v0:
                dq0.pop()
            dq0.append(j)
        if CM[j] != float('inf'):
            vM = CM[j] - P0[j]
            while dqM and CM[dqM[-1]] - P0[dqM[-1]] >= vM:
                dqM.pop()
            dqM.append(j)
    exp = i - b - 1
    if dq0 and dq0[0] == exp:
        dq0.popleft()
    if dqM and dqM[0] == exp:
        dqM.popleft()
    if dqM:
        C0[i] = P0[i] + CM[dqM[0]] - P0[dqM[0]]
    if dq0:
        CM[i] = PM[i] + C0[dq0[0]] - PM[dq0[0]]
res = min(C0[N], CM[N])
print(res if res != float('inf') else -1)