# 
import sys
sys.stdin=open("test.txt")
from collections import deque

def bfs(cur_x,cur_y):
    queue = deque([(cur_x,cur_y)])
    visited[cur_x][cur_y]=0
    while queue:
        x,y=queue.popleft()
        print("x,y:",x,y)
        if (x,y) == (door[1][0],door[1][1]):
            return visited[x][y]
        for dx,dy in direction:
            nx,ny = dx+x,dy+y
            print(nx,ny)
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==-1:
                if home[nx][ny]=="*":
                    continue
                if home[nx][ny]==".":
                    visited[nx][ny]=visited[x][y]
                elif home[nx][ny]=="!":
                    print("???")
                    if abs(x-y)==abs(nx-ny) or abs(x+y)==abs(nx+ny):
                        visited[nx][ny] = visited[x][y]
                    else:
                        visited[nx][ny]=visited[x][y]+1
                    
                else:
                    visited[nx][ny]=visited[x][y]
                queue.append((nx,ny))



N = int(input())
home = []
door=[]
for i in range(N):
    lst = list(input())
    for j in range(N):
        if lst[j]=="#":
            door.append((i,j))
    home.append(lst)
visited=[[-1 for _ in range(N)] for _ in range(N)]
direction = [(1,0),(0,-1),(-1,0),(0,1)]
print(home,door)
print(bfs(door[0][0],door[0][1]))
for row in visited:
    print(row)