import sys

input1 = sys.stdin.read().split()
if input1:
    idx = 0
    n = int(input1[idx])
    idx += 1
    last = {}
    used = set()
    for _ in range(n):
        t = int(input1[idx])
        url = input1[idx + 1]
        k = input1[idx + 2]
        u = input1[idx + 3]
        idx += 4
        if (t - last.get(u, -float('inf')) >= 5 and 
            url.startswith(("http://", "https://")) and 
            2 <= len(k) <= 12 and 
            k.isalnum() and 
            k not in used):
            used.add(k)
            last[u] = t
            print("YES")
        else:
            print("NO")