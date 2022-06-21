def solution(N, number):
    buf = [set() for _ in range(9)]

    for i in range(1,9):
        base_num = 0
        for j in range(0,i):
            base_num += N * pow(10,j)
        buf[i].add(base_num)
        for start, end in zip(range(1,i), range(i-1,0,-1)):
            for first in buf[start]:
                for second in buf[end]:
                    buf[i].add(first + second)
                    buf[i].add(first - second)
                    buf[i].add(first * second)
                if second != 0:
                    buf[i].add(first // second)

        if number in buf[i]:
            return i

    return -1