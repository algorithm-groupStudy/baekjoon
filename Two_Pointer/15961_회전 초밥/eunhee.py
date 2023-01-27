from collections import deque

n,d,k,c=map(int,input().split())
lst=deque([int(input()) for _ in range(n)])
queue=deque([])
idx=0
res=0
arr=[]
while 0<=idx<n:
    food=lst.popleft()
    queue.append(food)
    lst.append(food)
    if len(queue)==4:
        food_lst=list(set(list(queue)+[c]))
        arr.append(food_lst)
        res=max(res,len(food_lst))
        idx+=1
        queue.popleft()

print(res)