# 최대 bridge_length대(=길이), weight이하, "정해진 순서"
# 오르는 중은 무게 무시
# 건너는데 최소 몇초
# time 변수 계속 +1
# bridge에 0으로 비어있는 위치 표시해서 시뮬레이션
# 놓친 것 - cur_bridge pop할때 moving_truck도 같이 pop 했어야 함
# bridge에서 pop한게 0이라도 계속 검사 해야됨, 안그러면 한번에 하나씩만 움직임
# 2:08......
# 수정 - 완료 트럭이 필요할까?

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 1
    first = truck_weights.pop(0)
    cur_bridge = deque([0]*bridge_length)
    cur_bridge[0] = first
    moving_truck = [first]
    
    while moving_truck:
        current = cur_bridge.pop()
        if current != 0:
            moving_truck.pop(0)
            
        if (len(truck_weights) > 0 and
            truck_weights[0] + sum(moving_truck) <= weight and
             len(moving_truck) < bridge_length):
            new_truck = truck_weights.pop(0)
            cur_bridge.appendleft(new_truck)
            moving_truck.append(new_truck)
        else:
            cur_bridge.appendleft(0)

        time += 1
        
    return time