import sys
from collections import deque

sys.setrecursionlimit(200000)

input1 = sys.stdin.read().split()
n, m = int(input1[0]), int(input1[1])
grid = [input1[2 + i * m : 2 + (i + 1) * m] for i in range(n)]
s, t = 0, 1
head = [-1] * (2 * n * m + 2)
edges = []

def addEdge(u, v, cap):
    edges.append([v, cap, head[u]])
    head[u] = len(edges) - 1
    edges.append([u, 0, head[v]])
    head[v] = len(edges) - 1

for i in range(n):
    for j in range(m):
        u = i * m + j
        addEdge(2 + 2 * u, 3 + 2 * u, 1)
        char = grid[i][j]
        if char == 'a':
            addEdge(s, 2 + 2 * u, 1)
        elif char == 'd':
            addEdge(3 + 2 * u, t, 1)
        if char in 'abc':
            nxt = 'b' if char == 'a' else ('c' if char == 'b' else 'd')
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < m and grid[x][y] == nxt:
                    addEdge(3 + 2 * u, 2 + 2 * (x * m + y), 1)

flow = 0
while True:
    level = [-1] * len(head)
    level[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        e = head[u]
        while e != -1:
            v, cap, nxt = edges[e]
            if cap > 0 and level[v] == -1:
                level[v] = level[u] + 1
                q.append(v)
            e = nxt
    if level[t] == -1:
        break
    ptr = list(head)
    
    def dfs(u, f):
        if f == 0 or u == t:
            return f
        e = ptr[u]
        while e != -1:
            v, cap, nxt = edges[e]
            if level[u] + 1 == level[v] and cap > 0:
                pushed = dfs(v, min(f, cap))
                if pushed > 0:
                    edges[e][1] -= pushed
                    edges[e ^ 1][1] += pushed
                    return pushed
            ptr[u] = edges[e][2]
            e = ptr[u]
        return 0

    while True:
        pushed = dfs(s, float('inf'))
        if pushed == 0:
            break
        flow += pushed

print(flow)