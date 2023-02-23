N = int(input())
for n in range(1, N+1):
    # opcode 딕셔너리 
    opcode = {
        'ADD': '0000',
        'SUB': '0001',
        'MOV': '0010',
        'AND': '0011',
        'OR': '0100',
        'NOT': '0101',
        'MULT': '0110',
        'LSFTL': '0111',
        'LSFTR': '1000',
        'ASFTR': '1001',
        'RL': '1010',
        'RR': '1011'
    }

    code = input().split()
    res = ''

    # 상수 c를 사용하는 경우 (ADDC 등) 5번 bit에 1, 아닌 경우 0을 넣어준다 
    if code[0][-1] == 'C':
        res += opcode[code[0][:-1]] + '10'
    else:
        res += opcode[code[0]] + '00'
    
    # code[1]: rD, code[2]: rA, code[3]: rB 혹은 상수 #C 
    # f-string formatting으로 이진수로 바꾸고 앞자리는 0으로 채워줌 
    res += f'{int(code[1]):03b}'
    res += f'{int(code[2]):03b}'
    if code[0][-1] == 'C':
        res += f'{int(code[3]):04b}'
    else:
        res += f'{int(code[3]):03b}' + '0'

    print(res)