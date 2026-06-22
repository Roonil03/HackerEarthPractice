import sys

mod = 1000000007

def multiply(A, B):
    # C = [[0, 0], [0, 0]]
    # for i in range(2):
    #     for j in range(2):
    #         C[i][j] = (A[i][0] * B[0][j] + A[i][1] * B[1][j]) % mod
    # return C
    C = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for k in range(4):
            if A[i][k] == 0:
                continue
            for j in range(4):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

def power(A, p):
    # res = [[1, 0], [0, 1]]
    # base = A
    # while p > 0:
    #     if p & 1:
    #         res = multiply(res, base)
    #     base = multiply(base, base)
    #     p >>= 1
    # return res
    res = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    base = A
    while p > 0:
        if p & 1:
            res = multiply(res, base)
        base = multiply(base, base)
        p >>= 1
    return res

# def get_fib(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     T = [[1, 1], [1, 0]]
#     T_pow = power(T, n - 1)
#     return T_pow[0][0]

def get_sum(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n == 2:
        return 7    
    M = [
        [1, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]    
    Mp = power(M, n - 2)
    V2 = [4, 2, 1, 7]    
    res = 0
    for i in range(4):
        res = (res + Mp[3][i] * V2[i]) % mod
    return res

input1 = sys.stdin.read().split()
t = int(input1[0])
out = []
idx = 1
for _ in range(t):
    l = int(input1[idx])
    r = int(input1[idx+1])
    idx += 2
    res = (get_sum(r) - get_sum(l - 1)) % mod
    out.append(str(res))
print('\n'.join(out))