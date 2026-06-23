def solve (dim):
    # Write your code here
    dim = list(map(tuple, dim))
    W = sum(w for w, h in dim)
    H = sorted([0] + [h for w, h in dim])
    return [(W - w) * (H[-2] if h == H[-1] else H[-1]) for w, h in dim]
    
n = int(input())
dim = []
for _ in range(n):
    dim.append(map(int, input().split()))

out_ = solve(dim)
print (' '.join(map(str, out_)))