import sys

input1 = sys.stdin.read().split()
N = int(input1[0])
strings = input1[1:N+1]
tot = 0
for s in strings:
    tot += len(s)
MAX_NODES = tot + 1
t0 = [0] * MAX_NODES
t1 = [0] * MAX_NODES
nodeCount = 0
for s in strings:
    cur = 0
    for char in s:
        if char == '0':
            if not t0[cur]:
                nodeCount += 1
                t0[cur] = nodeCount
            cur = t0[cur]
        else:
            if not t1[cur]:
                nodeCount += 1
                t1[cur] = nodeCount
            cur = t1[cur]
dp1 = [0] * (nodeCount + 1)
dp2 = [0] * (nodeCount + 1)
C = [0] * (nodeCount + 1)    
sums = 0
for u in range(nodeCount + 1):
    n0 = t0[u]
    if n0:
        dp1[n0] = dp2[u] + 1
        dp2[n0] = dp1[u]
        C[n0] = C[u] + dp2[n0]
        sums = (sums + C[n0]) % 1000000007
    n1 = t1[u]
    if n1:
        dp1[n1] = dp1[u]
        dp2[n1] = 0
        C[n1] = C[u]
        sums = (sums + C[n1]) % 1000000007
print(sums % 1000000007)