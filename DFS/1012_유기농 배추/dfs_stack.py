T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
start_node = []
def dfs_stack(j,k):
    from collections import deque
    visit =[]
    queue = deque()
    #시작 노드 설정해주기
    queue.append([j,k])
    A[k][j]=0
     ## 방문이 필요한 리스트가 아직 존재한다면
    while queue:
       ## 시작 노드를 지정하고 
        node = queue.pop()
        x, y = node[0], node[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:    
                if A[ny][nx] ==1:           
                    if [nx,ny] not in visit:
                        A[ny][nx]=0
                        visit.append([nx,ny])
                        queue.append([nx,ny])
    return 1


for i in range(1,T+1):
    m, n, k = map(int, input().split())
    A = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        start_node.append([x,y])
        A[y][x] = 1
    cnt = 0
    for start in start_node:
        x,y = start[0], start[1]
        if A[y][x]==1:
            dfs_stack(x,y)
            cnt = cnt+1
    print(cnt)