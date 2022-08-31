# 장르별 노래 두개, 노래 순서 - 많이 재생된 장르, 장르 내에서는 많이 재생된 노래
# 장르 내에서 재생횟수 같으면 고유번호 낮은순
# 모든 장르는 재생횟수 다름
# 장르 안에 한곡밖에 없으면 하나만
# input genres - idx i의 장르(100미만), plays - idx i의 재생횟수 / 둘 길이는 동일, 1~10000
# output 노래 고유번호 i의 순서
# idea: hash로 그룹화?
# pseudo: hash로 각 장르별 재생 list 만듬
# 이후 각 장르별 재생횟수 계산
# 장르마다 상위 2개곡 빼와서 결과에 append, 그 이전에 고유번호순으로 정렬하기
# 풀이시간 1:21
from collections import defaultdict

def solution(genres, plays):
    answer = []
    table = defaultdict(list)
    play_count = defaultdict(int)
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        table[genre].append((idx,play))
        play_count[genre] += play
    for g in sorted(play_count.items(), key=lambda item: item[1], reverse=True):
         temp = sorted(table[g[0]], key=lambda x: x[1], reverse=True)
         if len(temp) > 1:
            answer.append(temp[0][0])
            answer.append(temp[1][0])
         else:
            answer.append(temp[0][0])
         
    return answer