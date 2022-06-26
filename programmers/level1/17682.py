# idea - 정규식? \d[S|D|T] | \d[S|D|T][\#|\*] ... > 길이가 달라 나눠지지가 않음... if 조건 어떻게?
# 얌전히 하나씩... 하나하나 꺼내서 조건 분기
#
# psuedo
# dartResult 빌때까지 반복
# pop후 임시변수에
# 변수 숫자면 점수 array에 넣어줌
# D|S|T면 현재 점수 계산
# #|*면 그에 맞는 계산 실행
# 막힌 점 - 10 나올때 처리
# 풀이시간 54분
# 다른 사람의 풀이 확인 후 - (\d+)([SDT])([*#]?) 처럼 정규식 사용 가능했음, match마다 () 세개써서 그룹으로 묶으면 되는듯
# 굳이 그룹 안묶어도 \d+[SDT][*#]? 면 매칭 가능함, +랑 ?의 사용법 익힐것
def solution(dartResult):
    answer = []

    dartResult = list(dartResult)

    while len(dartResult) > 0:
        temp = dartResult.pop(0)
        if temp.isdigit():
            if temp == "1" and dartResult[0] == "0":
                dartResult.pop(0)
                answer.append(10)
            else:
                answer.append(int(temp))
        elif temp == "D":
            answer[-1] = pow(answer[-1],2)
        elif temp == "T":
            answer[-1] = pow(answer[-1],3)
        elif temp == "*":
            if len(answer) > 1:
                answer[-1] *= 2
                answer[-2] *= 2
            else:
                answer[-1] *= 2
        elif temp == "#":
            answer[-1] *= -1

    return sum(answer)