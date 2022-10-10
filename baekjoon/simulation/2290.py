s, n = map(int, input().split())

def digit(s, input, number):
    if number in {1, 4}:
        input[0] +=   ' '*(s+2)
    else:
        input[0] +=   ' ' + '-'*s +   ' '
    for i in range(s):
        if number in {5, 6}:
            input[1+i] += '|' +   ' '*(s+1)
        elif number in {1, 2, 3, 7}:
            input[1+i] +=   ' '*(s+1) + '|'
        else:
            input[1+i] += '|' +  ' '*(s) + '|'
    if number in {1, 7, 0}:
        input[s+1] +=   ' '*(s+2)
    else:
        input[s+1] +=   ' ' + '-'*s +   ' '
    for i in range(s):
        if number in {2}:
            input[s+2+i] += '|' +   ' '*(s+1)
        elif number in {1, 3, 4, 5, 7, 9}:
            input[s+2+i] +=   ' '*(s+1) + '|'
        else:
            input[s+2+i] += '|' +  ' '*(s) + '|'
    if number in {1, 4, 7}:
        input[-1] +=   ' '*(s+2)
    else:
        input[-1] +=   ' ' + '-'*s +   ' '

answer = ['' for _ in range(s*2 + 3)]
for char in str(n):
    digit(s, answer, int(char))
    for i in range(len(answer)):
        answer[i] +=  ' '

for a in answer:
    print(a[:-1])