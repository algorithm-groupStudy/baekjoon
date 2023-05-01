import sys
sys.stdin = open("test.txt")

def clean(x,y):
    global total
    if not visited[x][y]:
            visited[x][y]=True
            total+=1

def check_around(x, y):
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and not board[nx][ny]:
            return True
        
    return False


def back(x,y,d):
    d_back = (d+2)%4
    nx,ny = x+dx[d_back], y+dy[d_back]
    if 0<=nx<N and 0<=ny<M and not board[nx][ny]:
        return nx,ny
    return False


def rotate(x,y,d):
    d_ninety = (d+3)%4
    nx,ny = x+dx[d_ninety],y+dy[d_ninety]
    if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and not board[nx][ny]:
        return (nx,ny,d_ninety)
    return x,y,d_ninety


dx = [-1, 0, 1, 0] #북, 동, 남, 서 # 위, 오른, 아래, 왼
dy = [0, 1, 0, -1]
total = 0
N, M = map(int, input().split())
r, c, d = map(int ,input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

while True:
    clean(r,c)
    if check_around(r,c):
        r,c,d = rotate(r,c,d)
    else:
        if not back(r,c,d):
            break
        r,c = back(r,c,d)

print(total)

