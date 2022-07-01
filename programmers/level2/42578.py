# 서로 다른 옷의 조합의 수
# 최대 조합수는 2^n -1(최소 한개의 의상)
# 모든 가능성 탐색하고 충돌나면 no count
# 탐색은 백트래킹
# 옷 하나 넣거나 안넣거나
# 하나 넣으면 count++
# 넣을때 충돌나면 탐색 중지
# 질문하기 참고 - 조합 구하는 걸로
# 1:24 - 풀이방법을 완전히 잘못잡음...


def solution(clothes):
    answer = 1
    spy = {x[1] : 1 for x in clothes}
    for c in clothes:        
        spy[c[1]] += 1
    for s in spy:
        answer *= spy[s]
    
    return answer - 1