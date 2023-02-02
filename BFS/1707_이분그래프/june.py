from collections import deque
def bfs(start,visited,arr):
    ## 연결 안되어 있는 노드처리 어떻게 할 것인 지 생각
    queue = deque()
    queue.append((start,1))                          # start 는 시작점의 숫자
    visited.append((start,1))               
    answer = 'Yes'                                    # 초기값 yes 지정 추후에 조건 만족시 no 로 변경가능
    set_list = []                       
    while queue:
        node = queue.popleft()                      # node = (v, check_num) 식으로 나옴   check_num 은 1과2 로 이분그래프 판별에 쓰일 예정
        vertex, check_num = node                    # 점의 숫자가 vertex , check_num
        set_list.append(vertex)                         # set_list 에 점 추가로 대입   이부분 중복되도 상관은 없겟지만 숫자 더 줄일방법 생각 ?
        check_num2 =(check_num+1)//check_num            # 예시를들면 check_num 이 1인경우 다음 check_num2 는 2가 되고 / check_num이 2이면 check_num2는 1이됨
                                                        # 2개의 집합으로 나누는 이분 그래프를 판별하는 기준이 됨
        for i in arr[vertex-1]:                           # arr[vertex-1] 은 vertex 와 연결된 점들이 모여있는 리스트가 됨  
            kkk = (i,check_num2)                            # kkk는 연결된 점 의미,  pop 한 노드와 한 기수 차이나는 노드들이므로 check_num 에서 check_num2  가됨
            if (i,check_num) in visited:                    # 예를 들어 연결된 점 kkk가  (2,2)일때  visited에 (2,1) 이 존재한다면 이분그래프가 성립하지 않으므로 answer 는 No 가 됨
                answer ='No'
                break
            if kkk not in visited:                  # 만약 연결된 점 kkk 가 visited 에 없다면 q 에 추가 
                queue.append(kkk)
                visited.append(kkk)
                
    return answer, set_list
    
T = int(input())
for tc in range(1,T+1):
    visited =[]
    check_set = set()
    v, e = map(int,input().split())
    check_visited = [0 for _ in range(v+1)]   # 인덱스의 편의를 위해서 +1
    adj_arr = [[] for _ in range(v)]
    for i in range(e):
        a, b = map(int,input().split())
        adj_arr[a-1].append(b)
        adj_arr[b-1].append(a)
                                                ### 선분이 연결된 것 표시해주는 이중리스트  [ [] ,[3] ,[2] ]   1과는 아무도 연결안됨, 2는 3과 연결, 3은 2와 연결 
    
    for i in range(1,v+1):                      ##  모든 점들에 대해서 탐색 / 점 1 부터 점V 까지
        if i not in check_set:                      ## 점이 check set에 없다면 bfs 실행
            answer, set_list = bfs(i,visited,adj_arr)     ### bfs 돌려서 나온 값인 yes or no 가 answer , check_set을 확장시켜줄 set_list 를 반환값으로 받음
            if answer == 'No':                                 ## 만약 answer 가 no면 더이상 할필요 없음
                break
            check_set = check_set.union(set(set_list))    # 그게 아니라면 bfs의 반환값인 set_list를 check_set 에 더해준다.
    print(answer)