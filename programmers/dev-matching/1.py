def solution(grade):
    answer = 0
    before = grade[-1]
    grade.reverse()
    for idx, g in enumerate(grade):
        if g > before:
            answer += g - before
            grade[idx] = before
        else:
            before = g
    return answer

print(solution([5,4,3,2,0]))