# BFS(너비 우선 탐색, Breath-First Search)
<p align="center"><img src='https://user-images.githubusercontent.com/94775103/212638046-513db143-36d0-43b0-887e-8679fe4debe5.gif' height="300px" width="300px"></p>

* **개념**  
: DFS와는 다르게 깊이가 아닌 넓이를 우선시 하여 탐색한다. 첫 시작 노드에서 연결된 노드를 다음 타겟으로 정하면서 진행된다.

* 장점
    - 출발노드에서 목표노드까지의 최단 길이 경로를 보장한다.
* 단점
    - 경로가 매우 길 경우에는 탐색 가지가 급격히 증가함에 따라 보다 많은 기억 공간을 필요로 하게 된다.
    - 해가 존재하지 않는다면 유한 그래프(finite graph)의 경우에는 모든 그래프를 탐색한 후에 실패로 끝난다.
    - 무한 그래프(infinite graph)의 경우에는 결코 해를 찾지도 못하고, 끝내지도 못한다.

## 소스 코드
### 2차원 배열 - Queue

```py
def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = [(x,y)]
    arr[x][y] = 0

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if arr[nx][ny] == 1:
                    queue.append((nx, ny))
                    arr[nx][ny] = 0
```

추가 내용) [참고-시간복잡도(Deque & List)](https://github.com/GGamangCoder/TIL/blob/main/%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84/Deque.md)
