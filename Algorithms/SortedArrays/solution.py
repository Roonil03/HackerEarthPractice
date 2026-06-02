import sys 

input1 = sys.stdin.read().split()
n = int(input1[0])
a = [int(x) for x in input1[1:n+1]]
moves = 0
for i in range(1, n):
    if a[i] <= a[i-1]:
        dif = a[i-1] + 1 - a[i]
        moves += dif
        a[i] = a[i-1] + 1
print(moves)