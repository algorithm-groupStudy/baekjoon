# 다시풀것
import sys
sys.stdin=open("test.txt")
n=int(input())
num_lst=list(map(int,input().split()))
res=[-1 for _ in range(n)]
stack=[]
for i in range(n):
    while stack and num_lst[stack[-1]]<num_lst[i]:
        res[stack.pop()]=num_lst[i]
    stack.append(i)
    
print(*res)


#시간 초과 코드 
# n = int(input())
# lst = list(map(int, input().split()))+[-1]
# stack = []
# for i in range(n):
#     idx = i
#     stack.append(lst[i])

#     while stack and idx < n and stack[-1] >= lst[idx]:
#         idx += 1

#     if stack and stack[-1] < lst[idx]:
#         stack.pop()
#         stack.append(lst[idx])
#         continue
#     stack.pop()
#     stack.append(lst[idx])
# print(*stack)