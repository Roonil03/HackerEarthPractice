import sys

d = sys.stdin.read().split()
idx = 1
for _ in range(int(d[0])):
    n = int(d[idx])
    a = [int(x) for x in d[idx+1:idx+1+n]]
    idx += n + 1
    j = c = 0
    while j < n:
        x = a[j]
        if a[j:j+x] != [x] * x:
            c = -1
            break
        c += 1
        j += x
    print(c if c >= 0 else "Invalid Data")