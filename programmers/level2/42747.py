# n편중 h번 이상 인용된 논문이 h이상, h최대값
# 인용횟수 들어올때 h-index return
# 인용횟수 0~10000, n은 1이상 1000 이하
# pseudo
# 인용횟수로 정렬, 가장 큰 논문 부터 시작
# 그냥 1씩 낮춰가면서 인용횟수 이상 리스트 크기 계산
# h번 이상이 h편 이상 조건 만족시 h인덱스
# 9, 8, 7, 1, 0
# 7편이상 3개 h:3
# 처음 9 - 1개, 8 - 2개, 7 - 3개(3번 이상이 3편 이상)
# 처음 9번 이상이 9번 이상 x, 8번 이상이 8번 이상 x, 7번 이상이 7번 이상 x, 
# 6, 5, 2, 1, 0
# 처음 6 - 1개, 5 - 2개, 2 - 3개(2번 이상이 2편 이상)
# 0,1,2,5,6
# 풀이시간 1:20

def solution(citations):
    for h in reversed(range(len(citations)+1)):
        h_size = len(list(filter(lambda x: x >= h, citations)))
        if h_size >= h:
            return h

# 아무리 봐도 효율성에 문제 있음...
# 다른 사람의 풀이 - sort 사용하는 방법

def solution(citations):
  sorted_citations = sorted(citations, reverse=True)
  for i in range(len(sorted_citations)):
    if sorted_citations[i] <= i: 
      return i
  return len(sorted_citations)
  # h자체는 동일하게 하나하나 계산하지만, 소팅으로 h보다 큰거 계산하는거를 없앰