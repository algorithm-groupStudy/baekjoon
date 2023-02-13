import sys
sys.stdin = open("test.txt")

n = int(input())
string = input()
cnt = 1
flag = False
color = string[0]
for i in range(n):
    if string[i] == color:
        flag = False
        continue
    else:
        if not flag:
            cnt += 1
        flag = True
print(cnt)
