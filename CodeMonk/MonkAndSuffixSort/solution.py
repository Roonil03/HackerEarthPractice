import sys

input1 = sys.stdin.read().split()
s, k = input1[0], int(input1[1])
print(sorted(s[i:] for i in range(len(s)))[k - 1])