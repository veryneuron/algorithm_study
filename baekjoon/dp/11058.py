# 코드 참고

N = int(input())
dp = [N for N in range(N+1)]

for i in range(6, N+1):
    dp[i] = max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)
print(dp[-1])