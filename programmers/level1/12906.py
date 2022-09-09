# 큐 사용, 중복시 안넣음
# pseudo
# 가장 끝 원소 확인
# 중복이면 스킵, 아니면 넣기
# 풀이시간 8:01

def solution(arr):
    answer = []
    for a in arr:
        if len(answer) > 0 and answer[-1] == a:
            continue
        else:
            answer.append(a)
    
    return answer