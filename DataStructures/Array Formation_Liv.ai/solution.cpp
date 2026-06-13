def queue_and_stack (A):
    # Write your code here
    A = list(A)
    m = max(A)
    p = [True] * (m + 1)
    p[0] = p[1] = False
    for i in range(2, int(m**0.5) + 1):
        if p[i]:
            p[i * i::i] = [False] * ((m - i * i) // i + 1)
    return [[x for x in A if p[x]], [x for x in reversed(A) if not p[x]]]
    
n = int(input())
A = map(int, input().split())

out_ = queue_and_stack(A)
for i_out_ in out_:
    print (' '.join(map(str, i_out_)))