# 주어진 동전으로 합 k원 만들기
# 어디서 많이 본문제? 그리디?
# 브루트 포스하면 아마 시간초과?
# dp의 느낌
# 각 경우의 수 계산해 보고 없는 결과 나오면 set에 넣기?
# 26:46 idea 참고...
# dp로 1부터 k원까지 가능한거 계산, 이전꺼 참고해서 재귀로
# 코드 출처 - https://mong9data.tistory.com/68


n, k = map(int, input().split())
coins = {int(input()) for _ in range(n)}
dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in coins:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
print(dp[k])