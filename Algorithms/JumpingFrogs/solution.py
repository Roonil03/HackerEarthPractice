import sys

input1 = sys.stdin.read().split()
h, p, q = map(int, input1)
if p >= h:
    print(1)
elif p <= q:
    print(-1)
else:
    print((h - q - 1) // (p - q) + 1)