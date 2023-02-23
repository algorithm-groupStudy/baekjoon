import sys
sys.stdin = open("text.txt")
n = int(input())
lst_A = list(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))
dic = {}
for i in lst_A:
    dic[i] = 1

for i in lst:
    if i in dic:
        print(1)
    else:
        print(0)
