import sys

input1 = sys.stdin.read().split()
a = [int(x) for x in input1[1:]]
a.sort()
res = 0
for i in range(0, len(a), 2):
    res += a[i]
print(res)