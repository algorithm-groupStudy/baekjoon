# BOJ 2468 안전 영역 

from collections import deque

def sol(arr, rain):
    count = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 특정 비의 양에 대하여 
    # 모든 영역에 대해 bfs를 실시, 잠기지 않는 영역을 구하고 visited에 저장, count +=1을해 준다. 
    for n in range(N):
        for m in range(N):
            if arr[n][m] > rain and visited[n][m]==0: 
                visited = bfs(n, m, arr, rain, visited)
                count += 1 
    return count

# BFS로 비에 잠기지 않는 영역 한 구역을 구한다. 
def bfs(si, sj, arr, rain, visited):
    q = deque([(si, sj)]) 
    visited[si][sj] = 1
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while q:
        i, j = q.popleft()
        for k in range(4): 
            ni = i + di[k]
            nj = j + dj[k]
            if (0 <= ni < N and 0 <= nj < N): 
                if visited[ni][nj] == 0 and arr[ni][nj] > rain: 
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    
    return visited



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 모든 영역이 잠기게 하는 비의 양 max_rain을 구한다. 
max_rain = max([max(l) for l in arr])
max_count = 0 
# 가능한 모든 비의 양에 관하여 잠기지 않은 영역을 세고,
# 잠기지 않은 영역이 가장 많을 때 이를 정답으로 한다. 
for rain in range(max_rain+1):
    count = sol(arr,rain)
    max_count = max(max_count, count)

print(max_count)