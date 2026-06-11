import sys

input1 = sys.stdin.read().split()
idx = 0
n = int(input1[idx])
q = int(input1[idx + 1])
idx += 2
a = [int(x) for x in input1[idx : idx + n]]
idx += n
events = [[] for _ in range(n + 2)]
for t in range(q):
    ty = int(input1[idx])
    if ty == 1:
        l, r, x = (
            int(input1[idx + 1]),
            int(input1[idx + 2]),
            int(input1[idx + 3]),
        )
        events[l].append((t, 1, x))
        events[r + 1].append((t, 1, -x))
        idx += 4
    else:
        l, r = int(input1[idx + 1]), int(input1[idx + 2])
        events[l].append((t, 2, 1))
        events[r + 1].append((t, 2, -1))
        idx += 3
M = 1
while M < q:
    M *= 2
tc = [0] * (2 * M)
ts = [0] * (2 * M)
tr = [0] * (2 * M)
ans = []
for i in range(1, n + 1):
    for t, ty, v in events[i]:
        pos = t + M
        if ty == 1:
            ts[pos] += v
        else:
            tc[pos] += v
        while pos > 1:
            pos >>= 1
            l = pos << 1
            r = l + 1
            tc[pos] = tc[l] + tc[r]
            ts[pos] = ts[l] + ts[r]
            tr[pos] = tr[l] + tr[r] + ts[l] * tc[r]
    ans.append(a[i - 1] * tc[1] + tr[1])
print(" ".join(map(str, ans)))