for _ in range(int(input())):
    n = list(f'{int(input()):b}')
    for idx, b in enumerate(reversed(n)):
        if b == '1':
            print(idx, end = ' ')