import sys
sys.stdin = open(r'C:\Users\byfor\OneDrive\바탕화~1-LAPTOP-OKI97V9F-10945\git\Algo\baekjoon\시뮬레이션&구현\input.txt')

opcode_dic = {
    'ADD' : '00000',
    'ADDC' : '00011',
    'SUB' : '00010',
    'SUBC' : '00011',
    'MOV' : '00100',
    'MOVC' : '00101',
    'AND' : '00110',
    'ANDC' : '00111',
    'OR' : '01000',
    'ORC' : '01001',
    'NOT' : '01010',
    'MULT' : '01100',
    'MULTC' : '01101',
    'LSFTL' : '01110',
    'LSFTLC' : '01111',
    'LSFTR' : '10000',
    'LSFTRC' : '10001',
    'ASFTR' : '10010',
    'ASFTRC' : '10011',
    'RL' : '10100',
    'RLC' : '10101',
    'RR' : '10110',
    'RRC' : '10111'
    }
t = int(input())

for test_case in range(1, t+1):
    # opcode rD rA rB 
    # opcode rD rA #C
    # rB 인지 #C 인지 판별 
    # 사용하지 않을 경우 000
    # 4번 비트가 0일 경우는 rB, 1일 경우는 #C
    assembly_code = list(input().split())
    binary_code = []
    binary_code += opcode_dic.get(assembly_code[0])
    
    # rD
    if assembly_code[1] == '0':
        binary_code += '0000'
    elif assembly_code[1] == '1':
        binary_code += '0001'
    elif assembly_code[1] == '2':
        binary_code += '0010'
    elif assembly_code[1] == '3':
        binary_code += '0011'
    elif assembly_code[1] == '4':
        binary_code += '0100'
    elif assembly_code[1] == '5':
        binary_code += '0101'
    elif assembly_code[1] == '6':
        binary_code += '0110'
    elif assembly_code[1] == '7':
        binary_code += '0111'
    # rA
    if assembly_code[0] == 'MOV' or assembly_code[0] == 'MOVC':
        binary_code += '000'
    elif assembly_code[0] == 'NOT':
        binary_code += '000'
    elif assembly_code[2] == '0':
        binary_code += '000'
    elif assembly_code[2] == '1':
        binary_code += '001'
    elif assembly_code[2] == '2':
        binary_code += '010'
    elif assembly_code[2] == '3':
        binary_code += '011'
    elif assembly_code[2] == '4':
        binary_code += '100'
    elif assembly_code[2] == '5':
        binary_code += '101'
    elif assembly_code[2] == '6':
        binary_code += '110'
    elif assembly_code[2] == '7':
        binary_code += '111'
    # rB or #C
    if binary_code[4] == '0': # rB
        if assembly_code[3] == '0':
            binary_code += '0000'
        elif assembly_code[3] == '1':
            binary_code += '0010'
        elif assembly_code[3] == '2':
            binary_code += '0100'
        elif assembly_code[3] == '3':
            binary_code += '0110'
        elif assembly_code[3] == '4':
            binary_code += '1000'
        elif assembly_code[3] == '5':
            binary_code += '1010'
        elif assembly_code[3] == '6':
            binary_code += '1100'
        elif assembly_code[3] == '7':
            binary_code += '1110'
    else: # #C
        # 아 이진수 변환시키는 함수 짤 걸 화난다.
        
        if assembly_code[3] == '0':
            binary_code += '0000'
        elif assembly_code[3] == '1':
            binary_code += '0001'
        elif assembly_code[3] == '2':
            binary_code += '0010'
        elif assembly_code[3] == '3':
            binary_code += '0011'
        elif assembly_code[3] == '4':
            binary_code += '0100'
        elif assembly_code[3] == '5':
            binary_code += '0101'
        elif assembly_code[3] == '6':
            binary_code += '0110'
        elif assembly_code[3] == '7':
            binary_code += '0111'
        elif assembly_code[3] == '8':
            binary_code += '1000'
        elif assembly_code[3] == '9':
            binary_code += '1001'
        elif assembly_code[3] == '10':
            binary_code += '1010'
        elif assembly_code[3] == '11':
            binary_code += '1011'
        elif assembly_code[3] == '12':
            binary_code += '1100'
        elif assembly_code[3] == '13':
            binary_code += '1101'
        elif assembly_code[3] == '14':
            binary_code += '1110'
        elif assembly_code[3] == '15':
            binary_code += '1111'
    for code in binary_code:
        print(code,end='')
    print()
    
    
    
    

