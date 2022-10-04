from collections import deque

T = int(input())
for _ in range(T):
    K, M, P = map(int, input().split())
    graph = [[] for _ in range(M)]
    in_graph = [[] for _ in range(M)]
    not_origin = []
    sequence = [1 for x in range(M)]
    for _ in range(P):
        source, destination = map(int, input().split())
        source -= 1
        destination -= 1
        graph[source].append(destination)
        in_graph[destination].append(source)
        not_origin.append(destination)
        sequence[destination] = -1
    
    dq = deque()
    for no in not_origin:
        dq.append(no)

    while dq:
        edge = dq.popleft()
        source_list = in_graph[edge]
        flag = False
        max_list = []
        max_val = -1
        for sl in source_list:
            if sequence[sl] == -1:
                flag = True
            if sequence[sl] > max_val:
                max_list.clear()
                max_list.append(sl)
                max_val = sequence[sl]
            elif sequence[sl] == max_val:
                max_list.append(sl)
        if flag:
            continue
        if len(max_list) == 1:
            sequence[edge] = max_val
        else:
            sequence[edge] = max_val + 1
        for g in graph[edge]:
            dq.append(g)
    print(K, sequence[-1])

# 다른 사람의 풀이 - 원래는 위상정렬 사용
# 위상정렬해서 큐 만들고 진입차수 기준으로 0인거부터 시작
# 연결된 진입차수 낮춰주면서 최대레벨 갱신