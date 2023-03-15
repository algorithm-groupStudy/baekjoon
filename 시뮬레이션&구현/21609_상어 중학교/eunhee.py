import sys
sys.stdin = open("test.txt")


def find_biggest(cur_x,cur_y,color,flag):
    queue = [(cur_x,cur_y)]
    visited[cur_x][cur_y] = True
    cnt = 1
    rainbow_cnt = 0
    if flag:
        board[cur_x][cur_y]=-100
    while queue:
        x,y = queue.pop(0)
        for dx,dy in d:
            nx, ny = dx + x, dy + y
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if board[nx][ny]==0:
                    rainbow_cnt+=1
                if board[nx][ny]==0 or board[nx][ny]==color:
                    if flag:
                        board[nx][ny]=-100
                    visited[nx][ny]=True
                    cnt+=1
                    queue.append((nx,ny))
    return cnt,rainbow_cnt

def reset_rainbow(lst,v):
    for i in range(n):
        for j in range(n):
            if lst[i][j]==0:
                v[i][j]=False
    return v

def remove_block(lst,flag):
    if flag:block_lst=[]
    else:block_lst=[[] for _ in range(n)]
    for i in range(n):
        cnt=0
        lst_copy=[]
        for j in range(n-1,-1,-1):
            if lst[j][i]==-100:
                cnt+=1
                continue
            elif lst[j][i]==-1:
                for _ in range(cnt):
                    lst_copy.append(-100)
                lst_copy.append(-1)
                cnt=0
            else:
                lst_copy.append(lst[j][i])
        for j in range(n-len(lst_copy)):
            lst_copy.append(-100)
        if flag:   # 90도로 돌렸을때
            lst_copy.reverse()
            block_lst.insert(0,lst_copy)
        else:    # 중력 작용만 했을때
            for i in range(n):
                block_lst[n-i-1].append(lst_copy[i])

    return block_lst



n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
d = [(0,1),(0,-1),(1,0),(-1,0)]
res = 0

while True:
    visited=[[False for _ in range(n)] for _ in range(n)]
    block_list=[]
    big = 0
    b_x, b_y=0,0
    for i in range(n):
        for j in range(n):
            if board[i][j]!=-1 and board[i][j]!=0 and board[i][j]!=-100 and not visited[i][j]:
                total,rainbow = find_biggest(i,j,board[i][j],False)
                if big<=total:
                    block_list.append((total,rainbow,i,j))
                    big=total
            visited=reset_rainbow(board,visited)
    if big<2:
        break
    block_list.sort(reverse=True)
    b_x, b_y=block_list[0][2],block_list[0][3]
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt,rainbow = find_biggest(b_x,b_y,board[b_x][b_y],True)
    res = res+cnt**2
    board = remove_block(board,True)
    board = remove_block(board,False)
print(res)
    
    