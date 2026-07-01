import sys

data = sys.stdin.read().split()
n = int(data[0])
c = data[1:n+1]
size = n + 1
is_int = [False] * size
for i in range(1, size):
    if len(c[i-1]) == len(set(c[i-1])):
        is_int[i] = True
adj = [[] for _ in range(size)]
idx = n + 1
for _ in range(n - 1):
    u = int(data[idx])
    v = int(data[idx+1])
    idx += 2
    adj[u].append(v)
    adj[v].append(u)
depth = [0] * size
parent = [0] * size
q_arr = [1]
visited = [False] * size
visited[1] = True
depth[1] = 1
head = 0
while head < len(q_arr):
    u = q_arr[head]
    head += 1
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            depth[v] = depth[u] + 1
            q_arr.append(v)
up = [0] * (19 * size)
min_int = [10**9] * (19 * size)
for i in range(1, size):
    up[i] = parent[i]
    if is_int[i]:
        min_int[i] = depth[i]
for k in range(1, 19):
    prev_offset = (k - 1) * size
    curr_offset = k * size
    for i in range(1, size):
        p = up[prev_offset + i]
        up[curr_offset + i] = up[prev_offset + p]
        m1 = min_int[prev_offset + i]
        m2 = min_int[prev_offset + p]
        min_int[curr_offset + i] = m1 if m1 < m2 else m2
comp_top = [0] * size
pref = [0] * size
for u in q_arr:
    if is_int[u]:
        comp_top[u] = 0
        pref[u] = pref[parent[u]]
    else:
        p = parent[u]
        if p == 0 or is_int[p]:
            comp_top[u] = u
        else:
            comp_top[u] = comp_top[p]
        
        t = comp_top[u]
        L = depth[u] - depth[t] + 1
        pref[u] = L * (L + 1) // 2 + pref[parent[t]]
q = int(data[idx])
idx += 1
out = []
for _ in range(q):
    orig_u = int(data[idx])
    orig_v = int(data[idx+1])
    idx += 2
    u, v = orig_u, orig_v
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for k in range(19):
        if (diff >> k) & 1:
            u = up[k * size + u]
    if u != v:
        for k in range(18, -1, -1):
            u_jump = up[k * size + u]
            v_jump = up[k * size + v]
            if u_jump != v_jump:
                u = u_jump
                v = v_jump
        w = up[u]
    else:
        w = u
    D = depth[orig_u] + depth[orig_v] - 2 * depth[w] + 1
    tot = D * (D + 1) // 2
    if is_int[w]:
        unint = pref[orig_u] - pref[w] + pref[orig_v] - pref[w]
    else:
        t = comp_top[w]
        pt = parent[t]
        dist_u = depth[orig_u] - depth[w]
        dI_u = 10**9
        if dist_u > 0:
            curr = orig_u
            for k in range(19):
                if (dist_u >> k) & 1:
                    val = min_int[k * size + curr]
                    if val < dI_u:
                        dI_u = val
                    curr = up[k * size + curr]
        depth_x = dI_u - 1 if dI_u != 10**9 else depth[orig_u]
        dist_v = depth[orig_v] - depth[w]
        dI_v = 10**9
        if dist_v > 0:
            curr = orig_v
            for k in range(19):
                if (dist_v >> k) & 1:
                    val = min_int[k * size + curr]
                    if val < dI_v:
                        dI_v = val
                    curr = up[k * size + curr]
        depth_y = dI_v - 1 if dI_v != 10**9 else depth[orig_v]
        Lx = depth_x - depth[t] + 1
        cy = (Lx * (Lx + 1)) // 2
        sum_bx = pref[orig_u] - pref[pt] - cy
        Ly = depth_y - depth[t] + 1
        cy2 = (Ly * (Ly + 1)) // 2
        sum_by = pref[orig_v] - pref[pt] - cy2
        Lxy = depth_x + depth_y - 2 * depth[w] + 1
        cxy = (Lxy * (Lxy + 1)) // 2
        unint = sum_bx + sum_by + cxy
    out.append(str(tot - unint))
sys.stdout.write('\n'.join(out) + '\n')