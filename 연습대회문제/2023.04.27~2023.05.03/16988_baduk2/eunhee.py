import sys
sys.stdin = open("test.txt")
from collections import deque
from itertools import combinations

def bfs_check(x,y):
    q = deque([(x,y)])
    visited[x][y] = True
    cnt = 1
    flag = True
    while q:
        nx,ny = q.popleft()
        for i in range(4):
            cx,cy = nx+dx[i], ny+dy[i]
            if 0<=cx<N and 0<=cy<M and not visited[cx][cy]:
                if board[cx][cy]==0:
                    flag = False    
                    # 0 이더라도 계속 탐색은 해야됨, 이 영역자체를 다 탐색하고 
                    # visited=False로 만듦으로 다음 턴에서 똑같은 영역을 
                    # 탐색하지 못하게 한다.
                if board[cx][cy]==2:
                    q.append((cx,cy))
                    visited[cx][cy]=True
                    cnt+=1
    return cnt if flag else 0

def set_baduk(lst): #바둑돌 놓기
    global visited
    x1, y1, x2, y2 = lst[0][0], lst[0][1], lst[1][0], lst[1][1]
    board[x1][y1] = 1
    board[x2][y2] = 1
    total = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j]==2:
                res = bfs_check(i,j)
                total+=res    # 두 덩어리로 나눠져 있는 경우가 있으므로 더하기
    board[x1][y1] = 0
    board[x2][y2] = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    return total

# def dfs_set(lst, idx):    # 바둑돌 놓을 위치 2곳 정하기  # 시간 초과
#     global res_total
#     if len(lst)==2:
#         res_total=max(set_baduk(lst),res_total)
#         # print("res_total:",res_total,"lst:",lst)
#     for i in range(idx, len(posLst)):
#         dfs_set(lst+[posLst[i]],i+1)


res_total = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
posLst = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            posLst.append((i,j))

for lst in list(combinations(posLst,2)):
    set_baduk(lst)
    res_total=max(set_baduk(lst),res_total)
print(res_total)
