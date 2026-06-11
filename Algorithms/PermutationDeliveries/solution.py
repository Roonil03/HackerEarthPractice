import sys

input1 = sys.stdin.read().split()
if not input1:
    sys.exit()
n = int(input1[0])
MOD = 998244353
MAX_PWR = 19
MAX_SZ = 1 << MAX_PWR
W = [1] * MAX_SZ
invW = [1] * MAX_SZ
wlen = pow(3, (MOD - 1) // MAX_SZ, MOD)
inv_wlen = pow(wlen, MOD - 2, MOD)
for i in range(1, MAX_SZ):
    W[i] = (W[i - 1] * wlen) % MOD
    invW[i] = (invW[i - 1] * inv_wlen) % MOD
REV = {}
def get_rev(sz):
    if sz in REV:
        return REV[sz]
    rev = [0] * sz
    j = 0
    for i in range(1, sz):
        bit = sz >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        rev[i] = j
    REV[sz] = rev
    return rev

def ntt(a, inv):
    sz = len(a)
    rev = get_rev(sz)
    for i in range(sz):
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]            
    length = 2
    while length <= sz:
        half = length // 2
        step = MAX_SZ // length
        w_arr = invW if inv else W        
        for i in range(0, sz, length):
            idx = 0
            for k in range(i, i + half):
                u = a[k]
                v = (a[k + half] * w_arr[idx]) % MOD
                a[k] = (u + v) % MOD
                a[k + half] = (u - v) % MOD
                idx += step
        length <<= 1        
    if inv:
        inv_n = pow(sz, MOD - 2, MOD)
        for i in range(sz):
            a[i] = (a[i] * inv_n) % MOD

def multiply(A, B):
    szA = len(A)
    szB = len(B)
    if szA * szB <= 1024:
        res = [0] * (szA + szB - 1)
        for i in range(szA):
            for j in range(szB):
                res[i + j] = (res[i + j] + A[i] * B[j]) % MOD
        return res        
    sz = 1
    while sz < szA + szB - 1:
        sz *= 2        
    a = A + [0] * (sz - szA)
    b = B + [0] * (sz - szB)
    ntt(a, False)
    ntt(b, False)
    for i in range(sz):
        a[i] = (a[i] * b[i]) % MOD
    ntt(a, True)
    return a[: szA + szB - 1]
polys = [[i, 1] for i in range(n)]
while len(polys) > 1:
    next_polys = []
    for i in range(0, len(polys), 2):
        if i + 1 < len(polys):
            next_polys.append(multiply(polys[i], polys[i + 1]))
        else:
            next_polys.append(polys[i])
    polys = next_polys
print(" ".join(map(str, polys[0][1:])))