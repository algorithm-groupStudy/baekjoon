from collections import deque
R , C = map(int,input().split())
A = [[] for _ in range(R)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
count =0

def dfs(x,y):
    stack =deque([x,y])
    visit = []
    visit.append(A[x-1][y-1])
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (1<=nx<=R and 1<=ny<=C):
                if A[nx-1][ny-1] not in visit:
                    count = count+1
                    stack.append([nx,ny])
                    visit.append(A[nx-1][ny-1])
                    dfs(nx,ny)
    return count
            
        


for i in range(R):
    alpha = input()
    for j in alpha:
        A[i].append(j)
print(dfs(1,1))