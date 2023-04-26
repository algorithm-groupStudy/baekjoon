import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        x,y,z = q.popleft()
        for i in range(6):
            nx,ny,nz = x+dx[i], y+dy[i], z+dz[i]
            if 0<=nx<H and 0<=ny<N and 0<=nz<M and not tomato_box[nx][ny][nz]:
                tomato_box[nx][ny][nz]=tomato_box[x][y][z]+1
                q.append((nx,ny,nz))


def find_tomato():
    res=0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato_box[i][j][k]==0:
                    return -1
                res=max(res,tomato_box[i][j][k])
    return res-1


dx=[-1,1,0,0,0,0]
dy=[0,0,0,0,-1,1]
dz=[0,0,-1,1,0,0]
M,N,H = map(int,input().split())

tomato_box = []
q=deque([])
for i in range(H):
    lst=[]
    for j in range(N):
        arr=list(map(int,input().split()))
        lst.append(arr)
        for k in range(M):
            if arr[k]==1:
                q.append((i,j,k))
    tomato_box.append(lst)

bfs()
print(find_tomato())