T = int(input())

for _ in range(T):
    controls = input()
    x_max, x_min, y_max, y_min = 0, 0, 0, 0
    degree = 0
    position = [0, 0]
    for control in controls:
        if control == 'F':
            if degree == 0:
                position[1] += 1
                y_max = max(y_max, position[1])
            elif degree == 90:
                position[0] += 1
                x_max = max(x_max, position[0])
            elif degree == 180:
                position[1] -= 1
                y_min = min(y_min, position[1])
            else:
                position[0] -= 1
                x_min = min(x_min, position[0])
        elif control == 'B':
            if degree == 0:
                position[1] -= 1
                y_min = min(y_min, position[1])
            elif degree == 90:
                position[0] -= 1
                x_min = min(x_min, position[0])
            elif degree == 180:
                position[1] += 1
                y_max = max(y_max, position[1])
            else:
                position[0] += 1
                x_max = max(x_max, position[0])
        elif control == 'R':
            degree = int((degree+90) % 360)
        elif control == 'L':
            if degree == 0:
                degree = 270
            else:
                degree -= 90
    print((x_max - x_min)*(y_max - y_min))

# 다른 사람의 풀이 - degree 자체에 위치 어디로 이동할건지 정보 담고 바로 더해버림