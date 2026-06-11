import sys
from collections import defaultdict

input1 = sys.stdin.read().split()
if input1:
    n = int(input1[0])
    m = int(input1[1])
    b = int(input1[2])
    idx = 3
    rows = defaultdict(set)
    for _ in range(b):
        rows[int(input1[idx])].add(int(input1[idx + 1]))
        idx += 2
    mx_e = (m + 1) // 2
    mn_e = (m + 2) // 3
    ans_mx = n * mx_e
    ans_mn = n * mn_e
    for r, cols in rows.items():
        ans_mx -= mx_e
        ans_mn -= mn_e
        prev = -1
        for c in sorted(cols):
            L = c - prev - 1
            if L > 0:
                ans_mx += (L + 1) // 2
                ans_mn += (L + 2) // 3
            prev = c
        L = m - prev - 1
        if L > 0:
            ans_mx += (L + 1) // 2
            ans_mn += (L + 2) // 3
    print(f"{ans_mx} {ans_mn}")