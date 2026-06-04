import sys

input_data = sys.stdin.read().split()
n, m = int(input_data[0]), int(input_data[1])
h = [int(x) for x in input_data[2 : 2 + n]]
c = [int(x) for x in input_data[2 + n : 2 + n + m]]
max_h = max(h) if h else 0
count = [0] * (max(max_h, m) + 2)
for x in h:
    count[x] += 1
f = [0] * (m + 1)
p, s = 0, n
for j in range(1, m + 1):
    f[j] = p + j * s
    p += j * count[j]
    s -= count[j]

def check(k):
    sub_c = sorted(c[:k], reverse=True)
    cur_sum = 0
    for j in range(1, k + 1):
        cur_sum += sub_c[j - 1]
        if cur_sum > f[j]:
            return False
    return True

low, high = 0, m
res = 0
while low <= high:
    mid = (low + high) // 2
    if check(mid):
        res = mid
        low = mid + 1
    else:
        high = mid - 1
print(res)