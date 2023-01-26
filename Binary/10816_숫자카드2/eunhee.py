# 메모리: 115304KB	시간: 740ms
n=int(input())
num_arr=list(map(int,input().split()))
m=int(input())
person=list(map(int,input().split()))

dic={}
for num in num_arr:
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1

print(*[dic[num] if num in dic else 0 for num in person])