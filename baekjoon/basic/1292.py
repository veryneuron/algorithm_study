A, B = map(int, input().split())

current = 1
counter = 1
result = 0

for i in range(1, B + 1):
    if i >= A:
        result += current
    if counter == current:
        current += 1
        counter = 1
    else:
        counter += 1

print(result)

# 다른 사람의 풀이(미리 리스트 만들기)

num_list = []

for i in range(50):
    num_list.extend([i]*i)

print(sum(num_list[A-1:B]))