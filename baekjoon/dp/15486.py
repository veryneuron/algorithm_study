# 아이디어 참고
import sys
input = sys.stdin.readline
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if i+lst[i][0] <= N:
        dp[i] = max(dp[i+lst[i][0]]+lst[i][1], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[0])