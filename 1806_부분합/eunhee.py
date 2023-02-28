import sys
sys.stdin = open("test.txt")
n, s = map(int, input().split())
num_lst = list(map(int,input().split()))
r=0
total = 0
length = 100001

for l in range(n):
    while total<s and r<n:
        total+=num_lst[r]
        r+=1
    num_len = r-l
    if total>=s:
        length = min(length,num_len)
    total-=num_lst[l]
if length==100001:
    length=0
print(length)