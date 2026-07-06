import sys

def distinctCharacter (S, arr, len):
    # write your code here
    p = [[0] * 26]
    for c in S:
        r = p[-1].copy()
        r[ord(c) - 97] += 1
        p.append(r)
    return [str(sum(p[R][i] > p[L - 1][i] for i in range(26))) for L, R in arr]

data = sys.stdin.read().split()
len = int(data[0])
S = data[1]
Q = int(data[2])
arr = [(int(data[i]), int(data[i+1])) for i in range(3, 3 + 2 * Q, 2)]

out_ = distinctCharacter(S, arr, len)
print (' \n'.join(out_))