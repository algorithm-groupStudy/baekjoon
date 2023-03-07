import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
field_size = int(input())
field = [list(map(int, input().split())) for _ in range(field_size)]

Graph = []
result = 1 
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 최대 높이 찾기 
max_height = 0
for i in range(field_size):
    graph.append(field[i])    
    for j in range(field_size):
        if field[i][j] >= max_height:
            max_height = field[i][j]
        

def dfs(x,y,num):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if field_size > nx >= 0 and field_size > ny >= 0 and visited[nx][ny] == 0:
            if graph[nx][ny] > num:
                visited[nx][ny] = 1
                dfs(nx, ny, num)

for i in range(max_height):
    visited =  [[0] * field_size for _ in range(field_size)]
    cnt = 0
    
    for j in range(field_size):
        for k in range(field_size):
            if graph[j][k] > i and visited[j][k] == 0:
                cnt += 1
                visited[j][k] = 1
                dfs(j,k,i)
    result = max(result, cnt)

print(result)