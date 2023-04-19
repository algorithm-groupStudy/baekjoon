import sys, collections

# 입력부
n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

# dx, dy : 방향배열(북, 남, 동, 서)
dx = [-1,1,0,0]
dy = [0,0,1,-1]

# open_x, open_y : 시작하는 문의 (x, y)좌표
open_x, open_y = -1, -1
# close_x, close_y : 끝나는 문의 (x, y)좌표
close_x, close_y = -1, -1

for i in range(n):
    for j in range(n):
        if arr[i][j] == '#':
            if open_x == -1 and open_y == -1:
                open_x, open_y = i, j
            else:
                close_x, close_y = i, j

# check : 현재 i행 j열이고 dir방향으로 들어올 때 필요한 최소 거울의 갯수
check = [[[-1] * 4 for _ in range(n)] for _ in range(n)]
q = collections.deque()

# 시작 지점에서 시작 방향 설정
for a in range(4):
    q.append((open_x, open_y, a))
    check[open_x][open_y][a] = 0
    
while q:
    x, y, dir = q.popleft()
    # 현재 지점이 닫는 문이면 정답 출력 후 바로 종료
    if x == close_x and y == close_y:
        print(check[x][y][dir])
        break
    nx, ny = x + dx[dir], y + dy[dir]
    # 범위에 만족하는 경우
    if 0 <= nx < n and 0 <= ny < n:
    
        # 벽이 아닌 경우
        if arr[nx][ny] != '*':
        
            # 처음 방문하는 곳이거나 이전에 방문했던 점보다 더 적은 횟수로 갈 수 있다면
            # 상태공간 갱신 및 큐의 앞부분에 삽입 
            # 거울을 놓을 수 있어도 놓지 않는 경우거나 아예 거울을 놓을 수 없는 공간 두 가지 모두 고려가능
            if check[nx][ny][dir] == -1  or check[nx][ny][dir] > check[x][y][dir]:
                check[nx][ny][dir] = check[x][y][dir]
                q.appendleft((nx, ny, dir))
                
            # 거울을 놓는 경우
            if arr[nx][ny] == '!':
                # 방향이 북이거나 남이면 동,서로 반사
                # 이 때 거울을 설치하기 때문에 큐의 뒷부분에 삽입
                if dir < 2:
                    for n_dir in range(2, 4):
                        if check[nx][ny][n_dir] == -1 or check[nx][ny][n_dir] > check[x][y][dir] + 1:
                            check[nx][ny][n_dir] = check[x][y][dir] + 1
                            q.append((nx, ny, n_dir))
                            
                # 방향이 동이거나 서라면 남,북으로 반사
                # 이 때 거울을 설치하기 때문에 큐의 뒷부분에 삽입
                else:
                    for n_dir in range(2):
                        if check[nx][ny][n_dir] == -1 or check[nx][ny][n_dir] > check[x][y][dir] + 1:
                            check[nx][ny][n_dir] = check[x][y][dir] + 1
                            q.append((nx, ny, n_dir))