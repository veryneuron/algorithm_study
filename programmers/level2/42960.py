# 알파벳 스타팅지점 - A*N
# 오락실게임 조이스틱
# 끝에서 끝으로 이동가능
# 1<=n<=20
# 최소 커서 이동 + 필요한 알파벳 변환 회수
# 알파벳 변환 횟수? 그냥 min (a에서 위로, a에서 아래로)
# 최소 커서 이동? 계속해서 제일 가까운 알파벳으로 이동!
# 가까운 알파벳 - 현재 기준에서 min(왼쪽으로계속, 오른쪽으로계속)
# 위치 이동하고 다시계산
# 1:45 풀이중지 - 정확성 81.5
# 문제가 그리디가 아님!!!


def solution(name):
    answer = 0
    cursor = 0
    unvisited = [x for x in list(name) if x != "A"]
    
    for _ in range(len(unvisited)):
        right_pos = cursor
        count_right = 0
        while name[right_pos] == "A":
            if right_pos == len(name)-1:
                right_pos = 0
            else:
                right_pos += 1
            count_right += 1
            
        
        left_pos = cursor
        count_left = 0
        while name[left_pos] == "A":
            if left_pos == 0:
                left_pos = len(name)-1
            else:
                left_pos -= 1
            count_left += 1
                
        answer += min(count_right, count_left)
        if count_right < count_left:
            cursor = right_pos
        else:
            cursor = left_pos
        
        alpha_up = ord("A")
        count_up = 0
        while chr(alpha_up) != name[cursor]:
            if chr(alpha_up) == "Z":
                alpha_up = ord("A")
            else:
                alpha_up += 1
            count_up += 1
                
            
        alpha_down = ord("A")
        count_down = 0
        while chr(alpha_down) != name[cursor]:
            if chr(alpha_down) == "A":
                alpha_down = ord("Z")
            else:
                alpha_down -= 1
            count_down += 1
        
        name = name[:cursor] + "A" + name[cursor+1:]
        answer += min(count_up, count_down)
        
    return answer