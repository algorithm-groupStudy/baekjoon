# DFS(깊이 우선 탐색, Depth-First Search)
<p align="center"><img src='https://user-images.githubusercontent.com/94775103/212637956-5b8112fa-d99c-41db-a89a-32c3a2b7d927.gif' height="300px" width="300px"></p>

* **개념**  
: 시작 노드에서 시작해서 다음 분기(branch)로 넘어가기 전에 **해당 분기를 완벽히 탐색 후** 다른 분기로 넘어가는 방식.  
: 여기서 분기는 갈림길이 있던 장소까지 되돌아간다는 것이다.  
: 이 알고리즘을 끝에서부터 부모노드로 돌아가는 것은 백트래킹(backtracking)이라고 한다.  
: 단순 검색 속도 자체는 BFS보다 느리다.

* 장점  
    - 단지 현 경로상의 노드들만을 기억하면 되므로 저장공간의 수요가 비교적 적다.  
    - 목표노드가 깊은 단계에 있을 경우 해를 빨리 구할 수 있다.  
* 단점
    - 해가 없는 경로에 깊이 빠질 가능성이 있다. 따라서 실제의 경우 미리 지정한 임의의 깊이까지만 탐색하고 목표노드를 발견하지 못하면 다음의 경로를 따라 탐색하는 방법이 유용할 수 있다.  
    - 얻어진 해가 최단 경로가 된다는 보장이 없다. 이는 목표에 이르는 경로가 다수인 문제에 대해 깊이우선 탐색은 해에 다다르면 탐색을 끝내버리므로, 이때 얻어진 해는 최적이 아닐 수 있다는 의미이다.   

## 소스 코드
### 2차원 배열 - Stack

```py
def dfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    stack, temp = [(x, y)], []
    arr[x][y] = 0
    j = 0

    while (stack or temp):
        if stack != []:
            x, y = stack.pop(-1)
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < M):
                    if arr[nx][ny] == 1:
                        stack.append((nx, ny))
                        temp.append((x, y))
                        arr[nx][ny] = 0
                        break
        elif temp != []:
            x, y= temp.pop(-1)
            stack.append((x, y))
```
