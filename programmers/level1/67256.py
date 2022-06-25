# idea: numbers 하나하나 따라가면서 손가락 위치 계속 이동
#
# pseudo
# numbers 순회하면서
# 1,3,7면 왼쪽 손가락 위치 변경
# 3,6,9면 오른쪽 손가락 위치 변경
# 0,8,5,2면 오른쪽 손가락 왼쪽 손가락 거리 비교하고 작은 쪽으로 손가락 위치 변경
# 이때 거리 같으면 hand로 판단
# 풀이시간 56분

table = {
     1 : (3,0), 2 : (3,1),  3 : (3,2),
     4 : (2,0), 5 : (2,1),  6 : (2,2),
     7 : (1,0), 8 : (1,1),  9 : (1,2),
    -1 : (0,0), 0 : (0,1), -2 : (0,2)
}

def solution(numbers, hand):
    answer = ''
    left_pos = -1
    right_pos = -2

    for n in numbers:
        if n in {1, 4, 7}:
            left_pos = n
            answer += "L"
        elif n in {3, 6, 9}:
            right_pos = n
            answer += "R"
        else:
            ldist, rdist = dist(left_pos,n), dist(right_pos,n)
            if ldist == rdist:
                if (hand == "left"):
                    left_pos = n
                    answer += "L"
                else:
                    right_pos = n
                    answer += "R"
            elif ldist < rdist:
                left_pos = n
                answer += "L"
            else:
                right_pos = n
                answer += "R"

    return answer

def dist(pos, num):
    return sum(list(tuple(abs(x-y) for x,y in zip(table[pos],table[num]))))