import sys
import itertools
import bisect

input1 = sys.stdin.read().split()

def h1(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

p = sorted(int("".join(x)) for s in ("1234", "1234567") for x in itertools.permutations(s) if h1(int("".join(x))))
o = []
for m in input1[1:]:
    idx = bisect.bisect_right(p, int(m))
    o.append(str(p[idx - 1]) if idx > 0 else "-1")
print('\n'.join(o))