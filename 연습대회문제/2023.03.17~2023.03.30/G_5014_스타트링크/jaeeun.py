# BOJ 5014 스타트링크

from collections import deque


def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        c = q.popleft()
        # S == G인 경우 1 리턴
        if c == G:
            return visited[c]
        # U 층 위로 가거나 D 층 아래로 갈 수 있다.
        for move in [U, -1*D]:
            n = c + move
            if 1 <= n <= F and visited[n]==0:
                q.append(n)
                visited[n] = visited[c] + 1
    # 이동 가능한 모든 층을 가도 G에 도달 못함
    return -1


F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F+1)]
res = bfs(S)
if res == -1:
    print("use the stairs")
else:
    # 출발층 1에서 시작하므로 정답은 -1 해준다.
    print(res-1)