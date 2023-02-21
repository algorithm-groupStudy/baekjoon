import sys
sys.stdin = open("text.txt")

dir = {"ADD": ["0000", "0"], "ADDC": ["0000", "1"], "SUB": ["0001", "0"],
       "SUBC": ["0001", "1"], "MOV": ["0010", "0"], "MOVC": ["0010", "1"], "AND": ["0011", "0"], "ANDC": ["0011", "1"], "OR": ["0100", "0"], "ORC": ["0100", "1"], "NOT": ["0101", "0"], "MULT": ["0110", "0"], "MULTC": ["0110", "1"], "LSFTL": ["0111", "0"], "LSFTLC": ["0111", "1"], "LSFTR": ["1000", "0"], "LSFTRC": ["1000", "1"], "ASFTR": ["1001", "0"], "ASFTRC": ["1001", "1"], "RL": ["1010", "0"], "RLC": ["1010", "1"], "RR": ["1011", "0"], "RRC": ["1011", "1"]}


def binary(n, num):
    string = bin(int(n))[2:]
    for i in range(num-len(string)):
        string = "0"+string
    return string


n = int(input())

for i in range(n):
    opcode, rD, rA, rB_rC = input().split()
    res = ""
    res += dir[opcode][0]
    res += dir[opcode][1]
    res += "0"
    res += binary(rD, 3)
    if opcode in ["MOV", "MOVC", "NOT"]:
        res += "000"
    else:
        res += binary(rA, 3)

    if res[4] == "0":
        res += binary(rB_rC, 3)+"0"
    else:
        res += binary(rB_rC, 4)
    print(res)
