# 알파벳

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

def bfs(x, y):
    queue = set([(x, y, graph[x][y])])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    ans = 1

    while queue:
        x, y, visited = queue.pop()
        ans = max(ans, len(visited))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                if graph[nx][ny] not in visited:
                    queue.add((nx, ny, visited + graph[nx][ny]))
    return ans

print(bfs(0, 0))