import sys

input_data = sys.stdin.read().split()
t = int(input_data[0])
idx = 1
out = []
for _ in range(t):
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    x = int(input_data[idx + 2])
    y = int(input_data[idx + 3])
    idx += 4
    res = min(n, (m + n * y) // (x + y))
    out.append(str(res))
sys.stdout.write("\n".join(out) + "\n")