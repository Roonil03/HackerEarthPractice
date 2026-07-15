import sys
from collections import Counter

input1 = sys.stdin.read().split()
k = int(input1[1])
c = [0] * 21
for i, v in Counter(input1[2:]).items():
    c[int(i) + 10 ] = v
for i in range(10):
    f = min(k, c[i])
    c[20 - i] += f
    c[i] -= f
    k -= f
if k % 2:
    for i in range(10, 21):
        if c[i]:
            c[20-i] += 1
            c[i] -= 1
            break
print(sum((i - 10) * c[i] for i in range(21)))
