import sys
import heapq

data = list(map(int, sys.stdin.read().split()))
n = data[0]
d, p = data[2 * n + 1], data[2 * n +2]
stat = sorted([(data[i], data[i+1]) for i in range(1, 2 * n, 2) if data[i] <= d], reverse=True)
heap = []
res = 0
cur = d
fuel = p
for s, f in stat + [(0, 0)]:
    while fuel < cur - s:
        if not heap:
            print(-1)
            exit
        fuel += -heapq.heappop(heap)
        res += 1
    fuel -= cur - s
    cur = s
    heapq.heappush(heap, -f)
print(res)