N = int(input())
signal = input()

order = int(N/5)
cross_signal = ['' for _ in range(order)]

for i in range(order):
    for j in range(5):
        cross_signal[i] += signal[i + order*j]

answer = ''
idx = 0
while idx < order:
    if cross_signal[idx] == '#####':
        if idx+1 < order:
            if cross_signal[idx+1] == '#...#':
                answer += '0'
                idx += 4
            elif cross_signal[idx+1] == '#.#.#':
                if cross_signal[idx+2] == '#####':
                    answer += '8'
                else:
                    answer += '6'
                idx += 4
            else:
                answer += '1'
                idx += 2
        else:
            answer += '1'
            break
    elif cross_signal[idx] == '#.###':
        answer += '2'
        idx += 4
    elif cross_signal[idx] == '#.#.#':
        answer += '3'
        idx += 4
    elif cross_signal[idx] == '###..':
        answer += '4'
        idx += 4
    elif cross_signal[idx] == '###.#':
        if cross_signal[idx+2] == '#.###':
            answer += '5'
        else:
            answer += '9'
        idx += 4
    elif cross_signal[idx] == '#....':
        answer += '7'
        idx += 4
    else:
        idx += 1

print(answer)