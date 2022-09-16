# 메모리 릭?
for _ in range(int(input())):
    arr = sorted(map(int, input().split()))
    print(arr[-3])

# pq 사용
# 메모리 사용량 더 많음...

import heapq

for _ in range(int(input())):
    arr = [-x for x in list(map(int, input().split()))]
    hq = []
    for a in arr:
        heapq.heappush(hq, a)
    heapq.heappop(hq)
    heapq.heappop(hq)
    print(abs(heapq.heappop(hq)))