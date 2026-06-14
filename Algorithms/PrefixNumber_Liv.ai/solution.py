def calculate (N):
    # Write your code here
    l = len(N)
    if l < 2:
        return 0
    if N[0] == '0':
        return 1 if N == "00" else 0       
    z, l1, r = [0] * l, 0, 0
    for i in range(1, l):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l1])
        while i + z[i] < l and N[z[i]] == N[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l1, r = i, i + z[i] - 1            
    return sum(1 for i in range(1, l // 2 + 1) if z[i] >= i)


N = input()

out_ = calculate(N)
print (out_)