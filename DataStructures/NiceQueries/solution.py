import sys
from bisect import bisect_left

input1 = sys.stdin.read().split()
n = int(input1[0])
q = int(input1[1])
ones = []
o1 = set()
idx = 2
out = []
for _ in range(q):
    qt = int(input1[idx])
    val = int(input1[idx+1])
    idx += 2
    if qt == 1:
        if val not in o1:
            o1.add(val)
            pos = bisect_left(ones, val)
            ones.insert(pos, val)
    else:
        pos = bisect_left(ones, val)
        if pos < len(ones):
            out.append(str(ones[pos]))
        else:
            out.append("-1")
print('\n'.join(out))