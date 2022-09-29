# 코드 참고 - https://velog.io/@lchyung1998/%EC%96%B4%EB%A0%A4%EC%9B%8C%EC%9A%94%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-BOJ-15989-1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0-4
# 1먼저 싹 더하고, 그다음 2랑 3 싹 계산해주면 됨
# 각 case에서 중복이 발생하지 않는 경우의 수 따질 수 있음


dp = [0 for _ in range(10001)]
dp[0] = 1
for i in range(1, 4):
    for j in range(i, 10001):
        dp[j] += dp[j-i]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])