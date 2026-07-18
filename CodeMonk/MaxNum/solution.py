import sys
import math

input1 = sys.stdin.read().split()
T = int(input1[0])
idx = 1
out = []
for _ in range(T):
		n, l = int(input1[idx]), int(input1[idx+1])
		idx += 2
		c = [0] * 30
		for i in range(idx, idx + n):
				a = int(input1[i])
				j = 0
				while a > 0:
						if a & 1:
								c[j] += 1
						a >>= 1
						j += 1
		idx += n
		w = [c[j] * (1 << j) for j in range(30)]
		w.sort(reverse=True)
		v = w[l-1]
		if v == 0:
				out.append("-1")
		else:
				out.append(str(math.comb(w.count(v), w[:l].count(v))))
print('\n'.join(out))