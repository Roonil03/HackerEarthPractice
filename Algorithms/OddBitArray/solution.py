import sys

input = sys.stdin.read
data = input().split()
idx = 0
t = int(data[idx])
idx += 1
MOD = 10**9 + 7
out = []
for _ in range(t):
	n = int(data[idx])
	idx += 1
	pp = 0
	e = 1
	o = 0
	dp = 0
	for _ in range(n):
		val = int(data[idx])
		idx += 1
		pc = bin(val).count("1")
		if pc % 2 != 0:
			pp ^= 1
		if pp == 0:
			dp = o
			e = (e + dp) % MOD
		else:
			dp = e
			o = (o + dp) % MOD
	out.append(str(dp))
print("\n".join(out))