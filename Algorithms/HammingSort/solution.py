import sys

input1 = sys.stdin.read().split()
idx = 0
t = int(input1[idx])
idx += 1
for _ in range(t):
    n = int(input1[idx])
    k = int(input1[idx + 1])
    idx += 2
    a = [int(x) for x in input1[idx : idx + n]]
    idx += n
    a.sort(key=lambda x: (bin(x ^ k).count("1"), x))
    print(" ".join(map(str, a)))