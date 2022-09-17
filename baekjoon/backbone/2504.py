# 스택

# 풀이 참조함, 쌓을 때 *, 닫을 때 이전꺼 동일한 짝일때만 더하는 것이 핵심
input = list(input())

stack = []
current = 1
result = 0

for i in range(len(input)):
    if input[i] == '(':
        stack.append(input[i])
        current *= 2
    elif input[i] == '[':
        stack.append(input[i])
        current *= 3
    elif input[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if input[i-1] == '(':
            result += current
        current //= 2
        stack.pop()
    else:
        if not stack or stack[-1] != '[':
            result = 0
            break
        if input[i-1] == '[':
            result += current
        current //= 3
        stack.pop()
if stack:
    print(0)
else:
    print(result)