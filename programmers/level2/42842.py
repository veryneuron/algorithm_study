# 노란색 격자 개수, 갈색 개수 기억 but 전체크기 x
# 중앙은 노란색, 테두리는 갈색
# return 전체크기
# 갈색 8이상, 노란색 1이상, 가로길이 >= 세로길이
# 가로, 세로 길이 <- 직사각형
# 노란색 가로로 일렬로
# 그 다음부터 노란색 한줄씩 늘려가면서 갈색 격자 확인
# 갈색 계산 - 노란색 가로길이*2 + 노란색 세로길이*2 + 4
# pseudo
# 가로길이 >= 세로길이 동안
# 1늘리고 나눠서 남는거 없을때
# 갈색 계산후 일치하면 return
# 풀이시간 38:47
def solution(brown, yellow):
    width = 0
    height = 0
    while width >= height:
        height += 1
        if yellow % height != 0:
            continue
        width = yellow / height
        result = width*2 + height*2 + 4
        if result == brown:
            return [width+2, height+2]
