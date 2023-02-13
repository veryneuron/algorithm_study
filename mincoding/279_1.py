# 홀수날 키1성장, 짝수날 키2성장, 안뿌릴수도있음
# 완전탐색... - x! 그리디?
# ㄴx! 2로 나눠 2의 개수 찾은 뒤 2개수와 1개수 비슷하게 2를 1로 쪼개줌!


TC = int(input())
answer = []
for _ in range(TC):
    N = int(input())
    heights = list(map(int, input().split()))
    water_list = list(map(lambda x: max(heights) - x, heights))
    num_of_2, num_of_1 = 0, 0
    for water in water_list:
        if water > 2:
            if (water % 2) == 1:
                num_of_1 += 1
            num_of_2 += water // 2
        elif water == 2:
            num_of_2 += 1
        elif water == 1:
            num_of_1 += 1
    # print(f"num1={num_of_1}, num2={num_of_2}")
    if num_of_1 > num_of_2:
        answer.append(num_of_1 * 2 - 1)
    elif num_of_1 == num_of_2:
        answer.append(num_of_1 * 2)
    else:
        diff = num_of_2 - num_of_1
        # print(f"diff={diff}")
        if (diff % 3) == 2:
            cali = (diff // 3) + 1
            # print(f"cali={cali}")
            answer.append((num_of_1 + cali * 2) * 2 - 1)
        else:
            cali = diff // 3
            answer.append((num_of_2 - cali) * 2)

for tc in range(TC):    
    print(f'#{tc+1} {answer[tc]}')