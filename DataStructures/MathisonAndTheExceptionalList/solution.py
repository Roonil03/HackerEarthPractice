import sys

input1 = sys.stdin.read().split()
if not input1:
    sys.exit()
n = int(input1[0])
idx = 1
bc = [0] * (n + 2)
bs = [0] * (n + 2)
last = {}
st = 1
out = []
for i in range(1, n + 1):
    e = int(input1[idx])
    l = int(input1[idx + 1])
    r = int(input1[idx + 2])
    idx += 3
    if e in last and last[e] + 1 > st:
        st = last[e] + 1
    last[e] = i
    length = i - st + 1
    curr = length
    while curr <= n:
        bc[curr] += 1
        bs[curr] += length
        curr += curr & (-curr)
    r = r if r < n else n
    if l > r:
        out.append("0")
        continue
    cr = sr = 0
    curr = r
    while curr > 0:
        cr += bc[curr]
        sr += bs[curr]
        curr -= curr & (-curr)
    cl = sl = 0
    curr = l - 1
    while curr > 0:
        cl += bc[curr]
        sl += bs[curr]
        curr -= curr & (-curr)
    ans = (sr - sl) - (cr - cl) * (l - 1) + (i - cr) * (r - l + 1)
    out.append(str(ans))
print("\n".join(out))