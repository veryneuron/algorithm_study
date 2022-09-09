# 명함 목록, 모든 명함 수납 가능, 크기 최소
# 가로 최대값, 세로 최대값 < 은 안됌
# 가로세로 값 바꾸기 가능
# 처음에 초기값 설정후 매번 가로세로 바꿔보면서 넣고 넓이저장 < x
# 길이차 이용
# 가로세로 바꿔보고 길이차 더 작은거로 변경
# pseudo
# 크기 하나라도 더 큰가 확인
# 길이차 비교후 더 작은거로 변경
# 풀이시간 35:35
def solution(sizes):
    width = 0
    height = 0
    for size in sizes:
        if size[0] > width or size[1] > height:
            rotated = max(0, size[0] - height) + max(0, size[1] - width)
            not_rotated = max(0, size[1] - height) + max(0, size[0] - width)

            if rotated > not_rotated:
                if size[0] > width:
                    width = size[0]
                if size[1] > height:
                    height = size[1]
            else:
                if size[0] > height:
                    height = size[0]
                if size[1] > width:
                    width = size[1]
                
    return width*height