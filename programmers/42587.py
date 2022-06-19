from collections import deque

def solution(priorities, location):
    answer = 1
    de = deque(priorities)
    max_val = max(de)

    while True:
        if de[0] < max_val:
            de.append(de.popleft())
            if location == 0:
                location = len(de)
            location -= 1
        else:
            if location == 0:
                return answer
            de.popleft()
            location -= 1
            answer += 1
            max_val = max(de)