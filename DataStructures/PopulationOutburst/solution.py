import sys

input1 = sys.stdin.read().split()
n = int(input1[0])
rcs = [int(input1[1])] + [0]*n
ids = [0] * (n + 1)
lvls = [0] * (n + 1)
out = []
pid = 0
count = 0
idx = 2
for i in range(1, n + 1):
    ids[i] = int(input1[idx])
    rcs[i] = int(input1[idx + 1])
    idx += 2
    while count == rcs[pid]:
        pid += 1
        count = 0
    count += 1
    lvls[i] = lvls[pid] + 1
    out.append(f"{ids[pid]} {lvls[i]} {count}")
sys.stdout.write("\n".join(out) + "\n")