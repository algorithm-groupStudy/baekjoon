from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))


distance = dict()
deck = deque()


distance[(0, 0)] = 1
deck.append((0, 0))
while deck:
    i, j = deck.popleft()
    if i == N-1 and j == M-1:
        break
    if i+1 < N and graph[i+1][j] == 1:
        if (i+1, j) not in distance:
            distance[(i+1, j)] = distance[(i, j)]+1
            deck.append((i+1, j))

    if j+1 < M and graph[i][j+1] == 1:
        if (i, j+1) not in distance:
            distance[(i, j+1)] = distance[(i, j)]+1
            deck.append((i, j+1))

    if i-1 >= 0 and graph[i-1][j] == 1:
        if (i-1, j) not in distance:
            distance[(i-1, j)] = distance[(i, j)]+1
            deck.append((i-1, j))

    if j-1 >= 0 and graph[i][j-1] == 1:
        if (i, j-1) not in distance:
            distance[(i, j-1)] = distance[(i, j)]+1
            deck.append((i, j-1))


print(distance[(N-1, M-1)])
