import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    n, q = int(data[0]), int(data[1])
    X = [0] * n
    P = [0] * n
    idx = 2
    for i in range(n):
        X[i] = int(data[idx])
        idx += 1
    for i in range(n):
        P[i] = int(data[idx])
        idx += 1
    max_A = [0] * (2 * n)
    max_B = [0] * (2 * n)
    for i in range(n):
        max_A[n + i] = X[i] + P[i]
        max_B[n + i] = X[i] + i + 1
    for i in range(n - 1, 0, -1):
        max_A[i] = max_A[2 * i] if max_A[2 * i] > max_A[2 * i + 1] else max_A[2 * i + 1]
        max_B[i] = max_B[2 * i] if max_B[2 * i] > max_B[2 * i + 1] else max_B[2 * i + 1]
    out = []
    INF = 10**18
    for _ in range(q):
        type = int(data[idx])
        if type == 1:
            pos = int(data[idx+1]) - 1
            x = int(data[idx+2])
            idx += 3
            X[pos] = x
            p = n + pos
            max_A[p] = x + P[pos]
            max_B[p] = x + pos + 1
            p //= 2
            while p > 0:
                max_A[p] = max_A[2 * p] if max_A[2 * p] > max_A[2 * p + 1] else max_A[2 * p + 1]
                max_B[p] = max_B[2 * p] if max_B[2 * p] > max_B[2 * p + 1] else max_B[2 * p + 1]
                p //= 2
        elif type == 2:
            pos = int(data[idx+1]) - 1
            p_val = int(data[idx+2])
            idx += 3
            P[pos] = p_val
            p = n + pos
            max_A[p] = X[pos] + p_val
            p //= 2
            while p > 0:
                max_A[p] = max_A[2 * p] if max_A[2 * p] > max_A[2 * p + 1] else max_A[2 * p + 1]
                p //= 2
        else:
            ql = int(data[idx+1]) - 1
            qr = int(data[idx+2]) - 1
            idx += 3
            C = ql + 1
            l = ql + n
            r = qr + n
            nodes = []
            while l <= r:
                if l % 2 == 1:
                    nodes.append(l)
                    l += 1
                if r % 2 == 0:
                    nodes.append(r)
                    r -= 1
                l //= 2
                r //= 2
            nb = [(max_A[node] if max_A[node] < max_B[node] - C else max_B[node] - C, node) for node in nodes]
            nb.sort(reverse=True)
            best = -INF
            for ub, node in nb:
                if ub <= best: break
                stack = [node]
                while stack:
                    curr = stack.pop()
                    if curr >= n:
                        val = max_A[curr] if max_A[curr] < max_B[curr] - C else max_B[curr] - C
                        if val > best: best = val
                        continue
                    left, right = 2 * curr, 2 * curr + 1
                    lb = max_A[left] if max_A[left] < max_B[left] - C else max_B[left] - C
                    rb = max_A[right] if max_A[right] < max_B[right] - C else max_B[right] - C
                    if lb > rb:
                        if rb > best: stack.append(right)
                        if lb > best: stack.append(left)
                    else:
                        if lb > best: stack.append(left)
                        if rb > best: stack.append(right)
            out.append(str(best))
    sys.stdout.write('\n'.join(out) + '\n')

solve()