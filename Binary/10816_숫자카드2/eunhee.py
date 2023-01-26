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

lst=[]
for num in person:
    if num in dic:
        lst.append(dic[num])
    else:
        lst.append(0)
print(*lst)