n=int(input())

top_lst=list(map(int,input().split()))
stack=[]

idx=0
while idx<n:
    if not stack : 
        stack.append((top_lst[idx],idx+1))
        print("0",end=" ")
        idx+=1
        continue
    if stack[-1][0]>top_lst[idx]:
        print(stack[-1][1],end=" ")
        stack.append((top_lst[idx],idx+1))
        
        idx+=1
    else:
        stack.pop()