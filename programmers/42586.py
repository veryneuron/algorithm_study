from collections import deque
import math

# no zip edition
def solution(progresses, speeds):
    round = deque([])
    answer = []

    for i in range(len(progresses)):
        round.append((100 - progresses[i]) // speeds[i])
        if ((100 - progresses[i]) % speeds[i] != 0):
            round[i] += 1
    
    while (len(round) > 0):
        temp = round.popleft()
        func = 1
        while ((len(round) > 0) and (round[0] <= temp)):
            round.popleft()
            func += 1
        answer.append(func)


    return answer

# zip editon
def solution_zip(progresses, speeds):
    answer = []
    temp = 0
    for p, s in zip(progresses, speeds):
        current = math.ceil((100-p)/s)
        if len(answer) == 0 or current > temp:
            answer.append(1)
            temp = current
        else:
            answer[-1] += 1
    
    return answer

