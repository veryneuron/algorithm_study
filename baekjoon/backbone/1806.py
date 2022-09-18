# 투 포인터

# 다른 사람 답변 참조

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = 0, 0
result = N+1
total = numbers[0]

while start <= end and end < N:
    if total < S:
        end += 1
        if end == N:
            break
        total += numbers[end]
    else:
        result = min(result, end - start + 1)
        total -= numbers[start]
        start += 1

if result == N+1:
    result = 0

print(result)