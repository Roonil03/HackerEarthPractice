import sys
from bisect import bisect_left

input1 = sys.stdin.read().split()
n = int(input1[0])
q = int(input1[1])
arr = [int(x) for x in input1[2:2+n]]
queries = input1[2+n:]
MAX_VAL = 20001
div = [[] for _ in range(MAX_VAL)]
for i in range(1, MAX_VAL):
    for j in range(i, MAX_VAL, i):
        div[j].append(i)
mul = [[] for _ in range(MAX_VAL)]
for idx, val in enumerate(arr, 1):
    for d in div[val]:
        mul[d].append(idx)            
out = []
ptr = 0
for _ in range(q):
    i = int(queries[ptr])
    x = int(queries[ptr+1])
    ptr += 2        
    if x >= MAX_VAL:
        out.append("0")
        continue            
    lst = mul[x]
    pos = bisect_left(lst, i)
    out.append(str(len(lst) - pos))
sys.stdout.write('\n'.join(out) + '\n')