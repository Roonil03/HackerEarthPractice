import sys

input1 = sys.stdin.read().split()
a = [int(x) for x in input1[1:]]
m = max(a)
fg = [True] * (m + 1)
if m >= 0:
    fg[0] = False
if m >= 1:
    fg[1] = False
for i in range(2, int(m ** 0.5) + 1):
    if fg[i]:
        for j in range(i * i, m + 1, i):
            fg[j] = False
prime = []
ot = []
for i in a:
    if fg[i]:
        prime.append(i)
    else:
        ot.append(i)
prime.sort()
ot.sort(reverse=True)
print(*(prime + ot))