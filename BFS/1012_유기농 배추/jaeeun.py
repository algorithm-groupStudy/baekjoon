from collections import deque 

def bfs(start, graph):
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    x, y = start 
    need_visit = deque([start])
    graph[x][y] = 0 
    while need_visit: 
        i, j = need_visit.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M: 
                if graph[ni][nj] == 1: 
                    need_visit.append((ni, nj))
                    graph[ni][nj] = 0 
            

T = int(input())

for tc in range(1, T + 1): 
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)] 
    for _ in range(K): 
        X, Y = map(int, input().split())
        arr[Y][X] = 1
    
    count = 0
    for n in range(N):
        for m in range(M): 
            if arr[n][m] == 1: 
                bfs((n, m), arr)
                count += 1 
    
    print(count)