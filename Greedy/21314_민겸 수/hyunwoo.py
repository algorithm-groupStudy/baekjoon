import sys
sys.stdin = open("/Users/hyunwoochoi/Desktop/python/sample_input.txt")

string = list(input())

m = 0
min_com = max_com = str()

for word in string:
    if word == 'M':
        m += 1
    elif word =='K':
        if m:
            max_com += '5' + '0' * m
            min_com += '1' + '0' * (m-1) + '5'
            m = 0
        else:
            max_com += '5' 
            min_com += '5'
if m:
    max_com += '1'+ '1'*(m-1)
    min_com += '1'+ '0'*(m-1)
    
print(max_com)
print(min_com)

