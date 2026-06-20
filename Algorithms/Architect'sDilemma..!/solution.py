import sys
input1 = sys.stdin.read().split()
n = int(input1[0])
w = int(input1[1])
a = [int(x) for x in input1[2:]]
a.sort()
j = 0
cost = 0
res = 0
for i in range(n):
    if i > j:
        cost += (a[i] - a[i-1]) * (i - j)
    while cost > w:
        cost -= (a[i] - a[j])
        j += 1
    if i - j + 1 > res:
        res = i - j + 1
print(res)