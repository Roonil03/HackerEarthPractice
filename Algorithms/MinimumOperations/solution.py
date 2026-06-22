def solve (N, A):
    """
    N: Represents the size of the array A
    A: Represents the elements of
    array A
    """
    s = sum(A)
    if s > 0:
        return -1
    k = -s
    res = sum((-x + 1) // 2 for x in A if x < 0)
    return k if res <= k else -1

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    out_ = solve(N, A)
    print (out_)