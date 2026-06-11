import sys

sys.setrecursionlimit(200000)

input1 = sys.stdin.read().split()
if input1:
    n = int(input1[0])
    idx = 1
    ops = []
    pts_set = set()
    for _ in range(n):
        op_type = int(input1[idx])
        if op_type == 0:
            x, y = int(input1[idx+1]), int(input1[idx+2])
            ops.append((0, x, y))
            pts_set.add((x, y))
            idx += 3
        else:
            ops.append((1, int(input1[idx+1]), int(input1[idx+2]), 
                        int(input1[idx+3]), int(input1[idx+4]), 
                        int(input1[idx+5]), int(input1[idx+6])))
            idx += 7

    pts = list(pts_set)
    K = len(pts)
    PT_X = [0] * K
    PT_Y = [0] * K
    LEFT = [-1] * K
    RIGHT = [-1] * K
    PARENT = [-1] * K
    MIN_X = [0] * K
    MAX_X = [0] * K
    MIN_Y = [0] * K
    MAX_Y = [0] * K
    INF = 10**18
    MAX_V1 = [-INF] * K
    MAX_V2 = [-INF] * K
    MAX_V3 = [-INF] * K
    MAX_V4 = [-INF] * K
    ACTIVE = [False] * K
    pt_to_node = {}

    def build(l, r, depth, p=-1):
        if l > r: return -1
        mid = (l + r) // 2
        if depth % 2 == 0:
            pts[l:r+1] = sorted(pts[l:r+1], key=lambda e: e[0])
        else:
            pts[l:r+1] = sorted(pts[l:r+1], key=lambda e: e[1])
        
        x, y = pts[mid]
        PT_X[mid] = x
        PT_Y[mid] = y
        PARENT[mid] = p
        pt_to_node[(x, y)] = mid
        
        LEFT[mid] = build(l, mid - 1, depth + 1, mid)
        RIGHT[mid] = build(mid + 1, r, depth + 1, mid)
        
        minx, maxx = x, x
        miny, maxy = y, y
        for c in (LEFT[mid], RIGHT[mid]):
            if c != -1:
                if MIN_X[c] < minx: minx = MIN_X[c]
                if MAX_X[c] > maxx: maxx = MAX_X[c]
                if MIN_Y[c] < miny: miny = MIN_Y[c]
                if MAX_Y[c] > maxy: maxy = MAX_Y[c]
        MIN_X[mid] = minx
        MAX_X[mid] = maxx
        MIN_Y[mid] = miny
        MAX_Y[mid] = maxy
        return mid

    root = build(0, K - 1, 0) if K > 0 else -1

    out = []
    for op in ops:
        if op[0] == 0:
            node = pt_to_node.get((op[1], op[2]), -1)
            if node != -1 and not ACTIVE[node]:
                ACTIVE[node] = True
                x, y = PT_X[node], PT_Y[node]
                v1, v2, v3, v4 = x+y, x-y, -x+y, -x-y
                curr = node
                while curr != -1:
                    changed = False
                    if v1 > MAX_V1[curr]: MAX_V1[curr] = v1; changed = True
                    if v2 > MAX_V2[curr]: MAX_V2[curr] = v2; changed = True
                    if v3 > MAX_V3[curr]: MAX_V3[curr] = v3; changed = True
                    if v4 > MAX_V4[curr]: MAX_V4[curr] = v4; changed = True
                    if not changed: break
                    curr = PARENT[curr]
        else:
            ans = -1
            if root != -1:
                qx, qy, x1, y1, x2, y2 = op[1], op[2], op[3], op[4], op[5], op[6]
                stack = [root]
                while stack:
                    node = stack.pop()
                    if node == -1 or MAX_V1[node] == -INF: continue
                    if MAX_X[node] < x1 or MIN_X[node] > x2 or MAX_Y[node] < y1 or MIN_Y[node] > y2: continue
                    
                    bp = MAX_V1[node] - qx - qy
                    v = MAX_V2[node] - qx + qy
                    if v > bp: bp = v
                    v = MAX_V3[node] + qx - qy
                    if v > bp: bp = v
                    v = MAX_V4[node] + qx + qy
                    if v > bp: bp = v
                    
                    if bp <= ans: continue
                    
                    if x1 <= MIN_X[node] and MAX_X[node] <= x2 and y1 <= MIN_Y[node] and MAX_Y[node] <= y2:
                        ans = bp
                        continue
                        
                    if ACTIVE[node]:
                        px, py = PT_X[node], PT_Y[node]
                        if x1 <= px <= x2 and y1 <= py <= y2:
                            dx = px - qx
                            if dx < 0: dx = -dx
                            dy = py - qy
                            if dy < 0: dy = -dy
                            d = dx + dy
                            if d > ans: ans = d
                            
                    stack.append(LEFT[node])
                    stack.append(RIGHT[node])
            if ans == -1:
                out.append("no point!")
            else:
                out.append(str(ans))
                
    print("\n".join(out))