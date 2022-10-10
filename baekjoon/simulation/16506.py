lines = [list(input().split()) for _ in range(int(input()))]

for line in lines:
    output = ''
    if 'ADD' in line[0]:
        output += '0000'
    elif 'SUB' in line[0]:
        output += '0001'
    elif 'MOV' in line[0]:
        output += '0010'
    elif 'AND' in line[0]:
        output += '0011'
    elif 'OR' in line[0]:
        output += '0100'
    elif 'NOT' in line[0]:
        output += '0101'
    elif 'MULT' in line[0]:
        output += '0110'
    elif 'LSFTL' in line[0]:
        output += '0111'
    elif 'LSFTR' in line[0]:
        output += '1000'
    elif 'ASFTR' in line[0]:
        output += '1001'
    elif 'RL' in line[0]:
        output += '1010'
    else:
        output += '1011'
    if 'C' in line[0]:
        output += '10'
        output += f'{int(line[1]):03b}'
        output += f'{int(line[2]):03b}'
        output += f'{int(line[3]):04b}'
    else:
        output += '00'
        output += f'{int(line[1]):03b}'
        output += f'{int(line[2]):03b}'
        output += f'{int(line[3]):03b}'
        output += '0'
    print(output)

# 다른 사람의 풀이
# 잘 보면 ADD - RR까지는 전부 0부터 23까지를 십육진수로 나타낸 것
# 따라서 이를 숫자로 바꾼 뒤 붙여줄 수 있음