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
	adj = [[] for _ in range (n+1)]
	for _ in range(n-1):
		u = int(data[idx])
		v = int(data[idx + 1])
		idx += 2
		adj[u].append(v)
		adj[v].append(u)
	guards = [0] * (n + 1)
	for i in range(1, n + 1):
		guards[i] = int(data[idx])
		idx += 1
	p = [0] * (n + 1)
	d = [0] * (n+1)
	s = [0] * (n+1)
	st = [1]
	p[1] = 0
	d[1] = 1
	s[1] = guards[1]
	vis = [False] *(n + 1)
	vis[1] = True
	order = []
	head = 0
	q = [1]
	while head < len(q):
		u = q[head]
		head += 1
		order.append(u)
		for v in adj[u]:
			if not vis[v]:
				vis[v] = True
				p[v] = u
				d[v] = d[u] + 1
				s[v] = s[u] + guards[v]
				q.append(v)
	LOGN = 21
	up = [[0] * LOGN for _ in range(n + 1)]
	for i in range(1, n + 1):
		up[i][0] = p[i]
	for j in range(1, LOGN):
		for i in range(1, n + 1):
			up[i][j] = up[up[i][j - 1]][j - 1]
	qq = int(data[idx])
	idx += 1
	for _ in range(qq):
		uu = int(data[idx])
		xx = int(data[idx + 1])
		idx += 2
		temp = s[uu]
		if xx > temp:
			out.append("1")
			continue
		cur = uu
		for j in range(LOGN - 1, -1, -1):
			anc = up[cur][j]
			if anc != 0:
				e = s[uu] - s[anc] + guards[anc]
				if xx > e:
					cur = anc
		if xx > guards[cur]:
			cur = p[cur]
		out.append(str(cur))
print("\n".join(out))