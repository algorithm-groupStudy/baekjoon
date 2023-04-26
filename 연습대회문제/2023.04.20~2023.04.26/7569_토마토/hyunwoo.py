from collections import deque

# Get input
m, n, h = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# Define directions
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# Initialize queue
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                queue.append((i, j, k))

# BFS
while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and boxes[nz][ny][nx] == 0:
            boxes[nz][ny][nx] = boxes[z][y][x] + 1
            queue.append((nz, ny, nx))

# Check if there are any unripe tomatoes
days = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 0:
                print(-1)
                exit()
            days = max(days, boxes[i][j][k])

# Print the number of days needed
print(days - 1)