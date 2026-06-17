import sys

input1 = sys.stdin.read().split()
n = int(input1[0])
m = 10**9+7
if n == 1:
    print(1)
    exit
fact = []
temp = n
if temp % 2 == 0:
    c = 0
    while temp % 2 == 0:
        c += 1
        temp //= 2
    fact.append((2, c))
d = 3
while d * d <= temp:
    if temp % d == 0:
        c = 0
        while temp % d == 0:
            c += 1
            temp //= d
        fact.append((d, c))
    d += 2
if temp > 1:
    fact.append((temp, 1))
d = 1
for _, v in fact:
    d *= (v + 1)
res = 1
for i, v in fact:
    base = (pow(i - 1, v , m) * pow(i, v * (v - 1) // 2, m)) % m
    res = (res * pow(base, d // (v + 1), m)) % m
print(res)