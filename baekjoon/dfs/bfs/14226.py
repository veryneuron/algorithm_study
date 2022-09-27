# from collections import deque

# S = int(input())

# answer = 1e9

# dq = deque()
# dq.append((0, 0, 1))
# done = [(0,1)]

# while dq:
#     time, clipboard, screen = dq.popleft()
#     if screen == S:
#         answer = time
#         break
#     if (screen, screen) not in done:
#         done.append((screen, screen))
#         dq.append((time+1, screen, screen))
#     if (clipboard, screen+clipboard) not in done and screen+clipboard <= S:
#         done.append((clipboard, screen+clipboard))
#         dq.append((time+1, clipboard, screen+clipboard))
#     if screen-1 >= 0 and screen-1 not in done:
#         done.append((clipboard, screen-1))
#         dq.append((time+1, clipboard, screen-1))

# print(answer)

# 6000ms...
# 다른 사람의 풀이 참고 - 딕셔너리로 최적화

from collections import deque

S = int(input())

answer = 1e9

dq = deque()
dq.append((0, 0, 1))
done = {}
done[(0,1)] = 0

while dq:
    time, clipboard, screen = dq.popleft()
    if screen == S:
        answer = time
        break
    if (screen, screen) not in done:
        done[(screen, screen)] = 0
        dq.append((time+1, screen, screen))
    if (clipboard, screen+clipboard) not in done and screen+clipboard <= S:
        done[(clipboard, screen+clipboard)] = 0
        dq.append((time+1, clipboard, screen+clipboard))
    if screen-1 >= 0 and (clipboard, screen-1) not in done:
        done[(clipboard, screen-1)] = 0
        dq.append((time+1, clipboard, screen-1))

print(answer)