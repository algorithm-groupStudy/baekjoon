from collections import deque


def move(c_lst,c_sum):
    global A_lst
    cal = int(c_sum/len(c_lst))
    for x,y in c_lst:
        A_lst[x][y]=cal


def bfs(x,y):
    global A_lst,visited
    queue = deque([(x,y)])
    visited[x][y]=True
    country_lst = [(x,y)]
    country_sum = A_lst[x][y]
    while queue:
        c_x,c_y = queue.popleft()
        for i in range(4):
            nx,ny = c_x+dx[i],c_y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if L<=abs(A_lst[c_x][c_y]-A_lst[nx][ny])<=R:
                    visited[nx][ny]=True
                    country_lst.append((nx,ny))
                    country_sum+=A_lst[nx][ny]
                    queue.append((nx,ny))
    return country_lst,country_sum


N, L, R = map(int,input().split())
A_lst = [list(map(int,input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

flag=False
res = 0    # 며칠 동안 발생하는지 결과 변수
while True:
    visited=[[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                c_lst, c_sum = bfs(i,j)
                if len(c_lst)>1:
                    flag=True
                    move(c_lst,c_sum)
    if not flag:
        break
    res+=1
    flag=False

print(res)


