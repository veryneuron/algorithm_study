# idea : board 세로로 가져온 뒤 큐라고 생각하고 moves마다 하나씩 인형 뽑아냄, 이전거랑 같으면 result+2
#
# pseudo
# 크기 n짜리 큐의 리스트 생성
# board iterate하면서 q에 원소 넣어줌
# iterate moves
# move에 해당하는 큐에서 원소 하나씩 꺼냄
# stored에 넣어줌, 만약 같으면 같이 제거하고 result +=2
# 풀이시간 1:17
# 풀이 후 - 굳이 zip으로 큐를 만들어서 사용해야됐을까? 그냥 2중포문으로 돌렸어도 됐을 것 같은데...

def solution(board, moves):
    answer = 0
    q = [[] for _ in range(len(board[0]))]
    bucket = []

    for idx, b in enumerate(zip(*board)):
        q[idx].extend(b)
        if 0 in q[idx]:
            q[idx] = list(filter(lambda x: x != 0, q[idx]))
            
    for m in moves:
        if len(q[m-1]) > 0:
            if len(bucket) == 0 or bucket[-1] != q[m-1][0]:
                bucket.append(q[m-1].pop(0))
            else:
                q[m-1].pop(0)
                bucket.pop()
                answer += 2        
    return answer