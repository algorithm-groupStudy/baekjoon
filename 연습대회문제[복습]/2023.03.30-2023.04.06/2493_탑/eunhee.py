import sys
sys.stdin=open("test.txt")

n = int(input())
top = list(map(int,input().split()))
stack = []
res=[0 for _ in range(n)]
for i in range(n-1,-1,-1):
    while stack and top[i]>top[stack[-1]]:
        res[stack.pop()]=i+1
    stack.append(i)
print(*res)