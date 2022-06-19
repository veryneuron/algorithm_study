def solution(n, lost, reserve):
    answer = 0

    clothes = [1] * n

    for l in lost:
        clothes[l-1] -= 1
    for r in reserve:
        clothes[r-1] += 1

    for i in range(n):
        if clothes[i] > 1:
            if i > 0 and clothes[i-1] == 0:
                clothes[i] -= 1
                clothes[i-1] += 1
            elif i < n-1 and clothes[i+1] == 0:
                clothes[i] -= 1
                clothes[i+1] += 1

    return len([x for x in clothes if x != 0])