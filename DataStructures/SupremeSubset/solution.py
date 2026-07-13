import sys
from collections import defaultdict

input1 = sys.stdin.read().split()
n, m = int(input1[0]), int(input1[1])
a = sorted(int(x) for x in input1[2:n+2])
d = defaultdict(list)
for x in a:
    d[x % m].append(x)
k = max(len(v) for v in d.values())
res = min(v for v in d.values() if len(v) == k)
print(k)
print(*res)
