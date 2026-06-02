import sys

input = sys.stdin.read
data = input().split()    
T = int(data[0])
idx = 1
out = []    
for _ in range(T):
	N = int(data[idx])
	A = [int(x) for x in data[idx+1 : idx+1+N]]
	idx += 1 + N        
	A.sort()
	min_xor = float('inf')
	for i in range(N - 1):
		val = A[i] ^ A[i+1]
		if val < min_xor:
			min_xor = val
	out.append(str(min_xor))        
print('\n'.join(out))