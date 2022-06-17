def solution(participant, completion):
    dict = {}
    answer = ''

    for part in participant:
        if part in dict:
            dict[part] += 1
        else:
            dict[part] = 1
    for comp in completion:
        dict[comp] -= 1
    for key, val in dict.items():
        if (val > 0):
            answer = key

    return answer