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
작은 숫자부터 탐색한다고 가정
[1] []


while문 시작


[2,5,9] [2,5]


[2,5,10] [2,5] [2]  


[2,6,8] [2,6] [2,7] [2]


[] [3] [] [4] []

## 소스 코드
### deque

```py
def dfs(graph, start_node):
    ## deque 패키지 불러오기
    from collections import deque
    visited = []
    need_visited = deque()
    
    ##시작 노드 설정해주기
    need_visited.append(start_node)
    
    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.pop()
 
        ##만약 방문한 리스트에 없다면
        if node not in visited:
 
            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
                
    return visited
```
* list 는 pop(0) 같은 연산에서 O(n) , deque 는 O(1) 

### 재귀함수
```py
def dfs_recursive(graph, start, visited = []):
## 데이터를 추가하는 명령어 / 재귀가 이루어짐 
    visited.append(start)
 
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited
```


