# 각 유저 - 한 번에 한 명 신고 가능, 횟수제한 x, 한 대상 중복 신고 가능하지만 1회로
# k번 이상 신고된 유저는 정지, 신고한 모든 유저에게 메일 발송
# purpose - 신고 처리 결과 메일 발송 시스템
# input - id_list(이용자 id)-list/1 이상, report("신고자 대상" 형태의 문자열 list)/1 이상, 각 문자열은 3 이상, 자기자신은 x/ k-정지기준, 자연수
# output - 각 유저가 받은 결과 메일 수 list / 이때 id_list의 순서가 유저의 순서임, 이에 맞게 출력해야됨
# 각 유저마다 누가 신고했는지 계산 후, k값 기준으로 자름, 이후 각 유저를 신고한 사람에게 메일 수 +1씩

# pseudo
# report 각 원소 파싱 후 [0]을 key로, [1]을 value로 해시 만듬 > **1을 key로!
# 만약 중복일시 pass
# 길이 k 이하인 해시 key 전부 제거
# id_list 순회함
# 순회하면서 그 값 key로 사용해서 있는 수만큼 result에 ++

# 풀이시간 52분
# 다른 사람 풀이 확인결과 in 뒤에 set(report) 처럼 사용 가능했음...

from collections import defaultdict
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    dict = defaultdict(set)

    for r in report:
        dict[r.split()[1]].add(r.split()[0])

    for id in id_list:
        if len(dict[id]) >= k:
            for i in dict[id]:
                answer[id_list.index(i)] += 1

    return answer