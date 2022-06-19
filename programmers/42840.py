def solution(answers):

    answer = []

    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]

    score1, score2, score3 = 0, 0, 0

    for i, ans in enumerate(answers):
        if ans == supo1[i % len(supo1)]:
            score1 += 1
        if ans == supo2[i % len(supo2)]:
            score2 += 1
        if ans == supo3[i % len(supo3)]:
            score3 += 1

    for i, score in enumerate([score1, score2, score3]):
        if score == max([score1, score2, score3]):
            answer.append((i+1, score)) # 굳이 따로 정렬 안하고 여기서 바로 index append하면 됨...

    return [x[0] for x in sorted(answer, key=lambda x : x[1])]

print(solution([1,2,3,4,5]))