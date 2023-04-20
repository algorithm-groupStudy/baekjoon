# BOJ 2151

from collections import deque 

def bfs(): 
    # map의 크기대로 check를 그림. 칸마다 상하좌우 정보(거울사용횟수)를 담는다 
    check = [[[-1]*4 for _ in range(N)] for _ in range(N)]
    for si, sj, sd in Q: 
        # 시작 좌표 및 방향: 거울을 아직 사용하지 않았으므로 0으로 초기화한다. 
        check[si][sj][sd] = 0 
    while Q: 
        ci, cj, cd = Q.popleft()  
        ni = ci + di[cd]   # cd 사용: 원래 가던 방향으로 직진? 
        nj = cj + dj[cd]
        if not (0 <= ni < N and 0 <= nj < N) or A[ni][nj] == '*': 
            continue 
        # 진행 가능한 경우 

        # 빈 공간인 경우 
        if A[ni][nj] == '.':
            if check[ni][nj][cd] == -1:  # 첫 방문인 경우 
                check[ni][nj][cd] = check[ci][cj][cd]  # 이전 좌표에서 사용한 거울 개수 유지 
                Q.append((ni, nj, cd))
            else:  # 이미 방문한 경우 
                if check[ni][nj][cd] > check[ci][cj][cd]:  # 거울 개수가 더 적은 쪽을 저장 
                    check[ni][nj][cd] = check[ci][cj][cd]
                    Q.append((ni, nj, cd))
        
        # 거울 설치 가능 공간인 경우 
        elif A[ni][nj] == '!':
            
            # 거울을 설치하지 않는 경우 (빈 공간과 동일)
            if check[ni][nj][cd] == -1:  # 첫 방문인 경우 
                check[ni][nj][cd] = check[ci][cj][cd]
                Q.append((ni, nj, cd))
            else: 
                if check[ni][nj][cd] > check[ci][cj][cd]:  # 거울 개수가 더 적은 쪽을 저장 
                    check[ni][nj][cd] = check[ci][cj][cd]
                    Q.append((ni, nj, cd))
            
            # 거울을 설치하는 경우 바뀐 방향에 저장 (가능한 방향은 두 개 ) 
            for nd in changeDir[cd]:
                if check[ni][nj][nd] == -1:  # 첫 방문 
                    check[ni][nj][nd] = check[ci][cj][cd] + 1 
                    Q.append((ni, nj, nd))
                else: 
                    if check[ni][nj][nd] > check[ci][cj][cd] + 1: 
                        check[ni][nj][nd] = check[ci][cj][cd] + 1 
                        Q.append((ni, nj, nd))


    temp = [] 
    for ck in check[gi][gj]:   # 도착 문에 저장된 최소 거울 개수 
        if ck == -1: 
            continue 
        temp.append(ck)
    return min(temp)                 
                
                 

N = int(input())
A = [] 
doors = [] 
for i in range(N): 
    A.append(list(input().split()))
    for j in range(N):
        if A[i][j] == '#':
            doors.append([i, j])  # 문 좌표를 찾는다 
            A[i][j] = '.' 

si, sj = doors[0]  # 시작 문 좌표 
gi, gj = doors[1]  # 도착 문 좌표 


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
changeDir = ((2, 3), (2, 3), (0, 1), (0, 1))  # ex) 위, 아래로 오는 경우 거울을 만나면 오른쪽, 왼쪽으로 방향을 바꾸게 된다. 

Q = deque() 
for k in range(4): 
    ni = si + di[k]
    nj = sj + dj[k]
    # 시작 좌표에서 출발 시 범위를 벗어나거나 벽인 방향을 제외하고 queue에 담아준다.  
    if not (0 <= ni < N and 0 <= nj < N) or A[ni][nj] == '*': 
        continue 
    Q.append((si, sj, k))

print(bfs()) 



