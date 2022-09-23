# 차량별 요금 계산, 기본요금 5000원 180분, 이후 10분마다 600원
# 파싱해서 각 차량별 누적 주차 시간 계산, 이후 정해진 공식 따라 주차 요금 계산
# 23:59까지 출차 안되어있으면 강제 출차
# 1:12

import math

def cal_diff(old, new):
    old_hour, old_min = int(old[0:2]), int(old[3:5])
    new_hour, new_min = int(new[0:2]), int(new[3:5])
    return (new_hour*60+new_min) - (old_hour*60+old_min)

def solution(fees, records):
    answer = []
    cars = {}
    payments = {}
    for record in records:
        time, car_no, log = record.split()
        if not car_no in cars:
            cars[car_no] = time
        else:
            old_time = cars[car_no]
            del cars[car_no]
            if car_no in payments:
                payments[car_no] += cal_diff(old_time, time)
            else:
                payments[car_no] = cal_diff(old_time, time)
    for key, value in cars.items():
        if key in payments:
            payments[key] += cal_diff(value, "23:59")
        else:
            payments[key] = cal_diff(value, "23:59")
    for _, time_value in sorted(payments.items()):
        if time_value <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((time_value - fees[0])/fees[2]) * fees[3])

    return answer