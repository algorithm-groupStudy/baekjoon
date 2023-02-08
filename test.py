import sys
sys.stdin=open("test.txt")
password_len, alphabet_count = map(int,input().split())
alphabet_list=list(map(str,input().split()))
alphabet_list = sorted(alphabet_list)
seq =[]
mo = set(['a','e','i','o','u'])

def dfs():
    count=0
    if len(seq) == password_len:
        for i in seq:
            if i in mo:
                count+=1
        if count>=1 and password_len-count>=2:
            print(''.join(map(str,seq)))
    for i in alphabet_list:
        if i not in seq:
            if seq==[]:
                seq.append(i)
                dfs()
                seq.pop(-1)
            elif i>seq[-1]:
                seq.append(i)
                dfs()
                seq.pop(-1)        
dfs()         