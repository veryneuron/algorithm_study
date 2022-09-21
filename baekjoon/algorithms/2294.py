# dp문제
# 동전1에서 가능한 가짓수 > 최소 가짓수로
# 동전 1에서처럼 문제 분할
# k원 -> 1~k원까지, 점화식은 k원 가짓수 구하기 위해서는 k-동전액수중에서 최소값 +1하면 됨

import sys

n, k = map(int, input().split())
coins = {int(input()) for _ in range(n)}
dp = [0 for _ in range(k+1)]

for i in range(1, k+1):
    q = sys.maxsize
    for c in coins:
        if i-c >= 0:
            q = min(q, dp[i-c])
    dp[i] = q + 1

if dp[k] >= sys.maxsize:
    print(-1)
else:
    print(dp[k])