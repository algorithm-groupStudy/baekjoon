import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
field_size = int(input())
field = [list(map(int, input().split())) for _ in range(field_size)]

graph = []
result = 1 
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 최대 높이 찾기 
max_height = 0
for i in range(field_size):
    for j in range(field_size):
        if field[i][j] >= max_height:
            max_height = field[i][j]

# 주변에 인접한 것이 없다면, visited 
def dfs(x,y,num):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if field_size > nx >= 0 and field_size > ny >= 0 and visited[nx][ny] == 0:
            if field[nx][ny] > num:
                visited[nx][ny] = 1
                dfs(nx, ny, num)

# 0부터 최대 높이까지의 모든 안전영역의 갯수 세기 
# for i in range(max_height):
#     visited =  [[0] * field_size for _ in range(field_size)]
#     cnt = 0  # 안전영역 갯수 초기화      
#     for j in range(field_size):
#         for k in range(field_size):
#             if field[j][k] > i and visited[j][k] == 0:
#                 cnt += 1
#                 visited[j][k] = 1
#                 dfs(j,k,i)
#     result = max(result, cnt)

for i in range(max_height):
    visited =  [[0] * field_size for _ in range(field_size)]
    cnt = 0  # 안전영역 갯수 초기화      
    for j in range(field_size):
        for k in range(field_size):
            if field[j][k] > i and visited[j][k] == 0:
                cnt += 1
                dfs(j,k,i)
    result = max(result, cnt)
print(result)
