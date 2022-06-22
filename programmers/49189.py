def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    q = [1]
    dist = [0 for _ in range(n+1)]

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    dist[1] = 1

    while q:
        cur = q.pop(0)
        for next in graph[cur]:
            if dist[next] == 0:
                q.append(next)
                dist[next] = dist[cur] + 1
    return dist.count(max(dist))

# BFS?
# BFS해서 가장 밑에 있는 node의 개수 <-어떻게 식별할까?
# BFS 구현은 큐를 사용
# visited 목록 필요
# 1. 모든 끝자락 노드의 depth 계산한 뒤 가장 큰 거의 갯수? <- 좀 낭비인거같기도?
# 2. 아니면 모든 노드까지의 거리를 구해...? <-더 낭비 ㅠㅠ
# input된 배열을 어떻게 사용할까?
# [[3, 6]
#  [4, 3]...] 형태로 들어옴
# 매번 검색? 좀 낭비같음...
# 차라리 각 edge에 연결된 edge 목록 쭉 리스트로 만드는게?
# 엣지는 어처피 n개까지 정해져 있으니, 1~n까지 나옴, 
# list를 iterate하면서 특정 원소 있으면 나머지 꺼 insert
# ++구현 중 notice! 재귀가 아니라 큐라 그냥 모든 거리 구해야 될 것 같음!
# ++depth는 어떻게? visited 체크할때 같이 넣으면 될듯? <- x, 큐가 이전에 추가된 거랑 새로 추가된 거랑 구분이 안됨...
# DFS?
# 해보니 안됨, 깊게 들어가는 기준이 트리가 아니라서 이상함
# 다시 BFS
# 수정! visited에 true false 넣는게 아니라 ,거리값 넣어서!
# ** 그래프 생성시 이상하게 만들면 시간초과 **
# 다른 사람 풀이 보니 그냥 visited 사용해도 됨, 거리 계산할때는 그냥 dist[j] = dist[i] + 1처럼...


# psuedo
# visited 초기화
# 연결 엣지목록 생성
#  ㄴ list 순회, 있으면 edge insert, 아니면 pass
# 1번 visited에 넣고 스타트
# 주변꺼 search(거리값이 있으면 안감, 아니면 go!) 후 큐에 넣음
# 현재 거리값 +1만큼 주변꺼에 거리값 할당해줌
# 최종적으로 거리 list에서 depth max인 것들 구해 count