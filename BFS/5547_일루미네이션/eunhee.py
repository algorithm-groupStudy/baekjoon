# 난 빡대가리인강.. 다음에 다시 한번 더 풀 문제!!!!!!!!!!!!!!!!

from collections import deque


def bfs(x, y):
    global visited, buildings
    queue = deque([(x, y)])
    visited[x][y] = True
    res = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in d[x % 2]:
            nx, ny = dx+x, dy+y
            if 0 <= nx < h+2 and 0 <= ny < w+2:
                if buildings[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif buildings[nx][ny] == 1:
                    res += 1
    return res


w, h = map(int, input().split())
buildings = [[0]+list(map(int, input().split()))+[0] for _ in range(h)]
buildings.insert(0, [0 for _ in range(w+2)])
buildings.append([0 for _ in range(w+2)])
visited = [[False for _ in range(w+2)] for _ in range(h+2)]
d = [[(-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1)],
     [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)]]
# 위에 한 줄 더 추가해줬으므로 홀수, 짝수 방향 바뀜.
# ** 한 줄 더 추가해 준 것을 고려하며 방향 계산을 해야됨.
# 홀수 짝수 방향 자꾸 틀림.
print(bfs(0, 0))
