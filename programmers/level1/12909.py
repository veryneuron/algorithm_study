# 스택 사용
# 암것도 없을 때 -> (만 가능
# 가장 위에 있는게 ( -> )만 가능
# 가장 위에 있는게 ) -> (만 가능 < 필요없음, 왜냐면 )는 생기면 스택에서 사라지기 때문!
# () 만날때마다 스택에서 삭제, 마지막에 스택 크기 0 확인
# 풀이시간 16:22

def solution(s):
    answer = True
    stack = []
    for par in s:
        if not stack and par == '(':
            stack.append(par)
        elif stack and stack[-1] == '(' and par == ')':
            stack.pop()
        else:
            stack.append(par)

    if not stack:
        return True
    else:
        return False
