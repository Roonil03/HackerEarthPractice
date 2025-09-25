# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    k = k % n
    rot = arr[-k:] + arr[:-k]
    print(*rot)