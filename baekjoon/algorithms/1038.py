# 큰 자릿수 -> 작은 자리수까지 계속 감소
# n번째 감소하는 감소하는 수
# 0은 0번째, 1은 1번째
# 가장 큰 감소하는 수? 9876543210
# 포기, 코드 참고... 출처 - https://velog.io/@imnotmoon/Python-%EB%B0%B1%EC%A4%80-1038.-%EA%B0%90%EC%86%8C%ED%95%98%EB%8A%94-%EC%88%98

from collections import deque

N = int(input())

numbers = deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

if N <= 9:
    print(N)
    exit()

count = 9

# 조합 + 큐

while numbers:
    recent = numbers.popleft()
    for i in range(10):
        if int(recent[-1]) <= i:
            break
        numbers.append(recent+str(i))
        count += 1
        if count == N:
            print(numbers[-1])
            exit()

print(-1)