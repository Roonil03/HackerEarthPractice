#complete this function to return a list that contains answer for all the queries of nodes
def solve(n , u , v , q , nodes):
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        adj[u[i]].append(v[i])
        adj[v[i]].append(u[i])    
    c = [0] * (n + 1)
    p = [0] * (n + 1)
    q = [1]
    vis = [False] * (n + 1)
    vis[1] = True    
    for cur in q:
        for nt in adj[cur]:
            if not vis[nt]:
                vis[nt] = True
                p[nt] = cur
                c[cur] += 1
                q.append(nt)                
    res = [0] * (n + 1)
    res[1] = c[1]    
    for cur in q[1:]:
        res[cur] = res[p[cur]] + c[cur] - 1        
    return [res[x] for x in nodes]
    
n = eval(input())
u = list(range(n))
v = list(range(n))
for i in range(0,n-1):
    u[i],v[i] = list(map(int, input().split()))

q = eval(input())
nodes = list(range(q))
for i in range(0,q):
    nodes[i] = eval(input())

ans = solve(n , u , v , q, nodes)
for x in ans:
    print(x)