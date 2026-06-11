import sys
 
input1 = sys.stdin.read().split()
n = int(input1[0])
a = [int(x) for x in input1[1 : 1 + n]]
first = {}
res = cur = 1 if n > 0 else 0
for i in range(n):
    x = a[i]
    if x not in first:
        first[x] = i
    dist = i - first[x] + 1
    if dist > res:
        res = dist
print(res)