N = int(input())
block = list(input())
dp = [-1 for _  in range(N)]
dp[0] = 0

for i in range(N):
    if dp[i] != -1:
        for j in range(i+1, N):
            if ((block[i] == 'B' and block[j] == 'O') or
                (block[i] == 'O' and block[j] == 'J') or
                (block[i] == 'J' and block[j] == 'B')):
                if dp[j] == -1:
                    dp[j] = dp[i] + (j-i)**2
                else:
                    dp[j] = min(dp[j], dp[i] + (j-i)**2)
print(dp[-1])