def check_direction(x,y):
    direct=[0,0,0,0]    # 해당 방향으로 갔을때 전선의 길이, 중간에 코어가 있으면 0으로 표시
    for dx in range(4):
        nx,ny = x,y
        length = 0
        while 0<nx<n-1 and 0<ny<n-1:
            length+=1
            nx+=d[dx][0]
            ny+=d[dx][1]
            if board[nx][ny]==1:
                break
        else:
            direct[dx]=length    # 중간에 코어가 없으면 지금까지 센 전선의 길이 넣어주기
    return direct

def connect(x,y,direct):
    global board
    nx,ny = x,y
    while 0<nx<n-1 and 0<ny<n-1:    # 전선 연결한 코어, 전선연결된 곳은 1로 처리해주기
        nx+=d[direct][0]
        ny+=d[direct][1]
        board[nx][ny]=(board[nx][ny]+1)%2   
        
    

def dfs(cnt,min_sum,res_cnt):    # cnt: 재귀돌은 횟수, min_sum: 선 길이, res_cnt: 연결된 코어 수
    global result
    if res_cnt>result[1]:    # 연결된 코어의 수가 res_cnt에 담긴 숫자보다 클 때,
        result[1]=res_cnt
        result[0]=min_sum
    elif res_cnt==result[1] and min_sum<result[0]:    # 코어수는 같지만, 전선길이는 더 짧을때
        result[0]=min_sum
    if cnt==core_cnt:    # cell에 있는 코어를 다 겠을 경우
        return
    x,y = core_lst[cnt][0],core_lst[cnt][1]    # 현재 core_lst에 담긴 좌표
    direction = check_direction(x,y)    #
    for k in range(4):
        if not direction[k]:
            continue
        connect(x,y,k)    # 연결
        dfs(cnt+1,min_sum+direction[k],res_cnt+1)
        connect(x,y,k)    #연결 끊기
    dfs(cnt+1,min_sum,res_cnt)    # 연결할 선이 없을경우, 선을 연결하지 않고 다음으로 가기


t = int(input())
for tc in range(1,t+1):    # 테스트 케이스만큼 반복
    n=int(input())
    board=[list(map(int,input().split())) for _ in range(n)]    # N*N cell
    d = [(1,0),(-1,0),(0,1),(0,-1)]   #  가로세로 탐색 위한 방향
    core_lst=[]    # 코어가 담긴 리스트
    core_cnt = 0    # 코어 숫자, 코어만큼 탐색하기 위해. (depth == core_cnt 일때 return)
    res = 145
    for i in range(1,n):
        for j in range(1,n):
            if board[i][j]==1:
                core_lst.append((i,j))
                core_cnt+=1

    result = [0,0]    # result[0] : 전선 길이, result[1]코어의 수
    # 1) 최대한 많은 core를 연결, 2) 전선 최소 길이
    dfs(0,0,0)
    print(f"#{tc} {result[0]}")


    


