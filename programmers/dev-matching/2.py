# hori~에 따라 처음 수직 수평
# 움직일 때 마다 count++
# 맨 처음에는 1


def solution(n, horizontal):
    answer = [[-1]*n for x in range(n)]
    current = 0
    count = 2

    answer[0][0] = 1
    while True:
        if horizontal:
            horizontal = False
        else:
            horizontal = True
        current += 1
        if current == n:
            break
        count = clean(current, answer, count, horizontal)

    return answer

def clean(current, answer, count, horizontal):
    if horizontal:
        for y in range(current+1):
            answer[current][y] = count
            count += 1
        for x in range(current-1, -1, -1):
            answer[x][current] = count
            count += 1
    else:
        for x in range(current+1):
            answer[x][current] = count
            count += 1
        for y in range(current-1, -1, -1):
            answer[current][y] = count
            count += 1
    return count