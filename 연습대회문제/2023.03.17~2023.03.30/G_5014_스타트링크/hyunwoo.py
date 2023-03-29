import sys
sys.stdin = open('input.txt')

from collections import deque

floors, start, goal, up, down = map(int, input().split())

def bfs(start, goal):
    q = deque()
    visited = [-1] * (floors + 1) # 
    q.append(start)
    visited[start] = 0

    while q:
        x = q.popleft()
        if x == goal:
            return visited[x]
        
        for new_x in (x + up, x - down):
            if 0 < new_x <= floors and visited[new_x] == -1:
                q.append(new_x)
                visited[new_x] = visited[x] + 1
    return "use the stairs"


print(bfs(start, goal))
