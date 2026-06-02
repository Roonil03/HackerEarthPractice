from collections import defaultdict
import sys

input = sys.stdin.read().split()
n = int(input[0])
m = int(input[1])
k = int(input[2])
intervals = defaultdict(list)
idx = 3
for _ in range(n):
    l = int(input[idx])
    r = int(input[idx + 1])
    z = int(input[idx + 2])
    intervals[z].append((l, r))
    idx += 3
events = defaultdict(int)
for z in intervals:
    intervals[z].sort()
    merged = []
    for l, r in intervals[z]:
        if not merged or merged[-1][1] < l:
            merged.append([l, r])
        else:
            merged[-1][1] = max(merged[-1][1], r)
    for l, r in merged:
        events[l] += 1
        events[r + 1] -= 1
events[m + 1] += 0
res = 1
mod = 1000003
lpos = 1
f = 0
for pos in sorted(events.keys()):
    if pos > lpos:
        length = min(pos, m + 1) - lpos
        choices = max(0, k - f)
        res = (res * pow(choices, length, mod)) % mod
        lpos = min(pos, m + 1)
    f += events[pos]
    if lpos == m + 1:
        break
print(res)
