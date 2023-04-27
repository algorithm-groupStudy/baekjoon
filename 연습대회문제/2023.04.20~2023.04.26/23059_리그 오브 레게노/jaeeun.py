# BOJ 23059 리그 오브 레게노 
import heapq
import sys 
input = sys.stdin.readline


# 위상정렬 사용 (우선순위 큐로 진입차수가 0인 노드들이 사전 순으로 출력되게 함 )
def topology_sort(V):
    result = [] 
    q = [] 
    for i in range(V):
        if indegree[i] == 0:
            heapq.heappush(q, [item_index[i], i]) 
            
    
    temp = []
    while q:
        now_item, now_idx = heapq.heappop(q)
        result.append(now_item)
        for i in graph[now_idx]:
            indegree[i] -= 1 
            if indegree[i] == 0:
                temp.append(i)
        
        # 현재 구매할 수 있는 아이템을 모두 찾아 사전 순으로 구매하므로 q가 비었을 때 구매 가능한 아이템을 한꺼번에 모두 push해주었다. 
        if not q: 
            for i in temp: 
                heapq.heappush(q, [item_index[i], i]) 
            temp = []

    
    if len(result) == V: 
        return result 
    else:
        return -1 



N = int(input().rstrip())
# 딕셔너리를 이용해 item이름:item index 저장 
items = dict() 
cnt = 0 

indegree = [0] * (N*2)
graph = [[] for i in range(N*2)]

for _ in range(N):
    a_item, b_item = input().split()
    if a_item in items: 
        a = items[a_item]
    else:
        items[a_item] = cnt
        a = cnt  
        cnt += 1 

    if b_item in items: 
        b = items[b_item]
    else:
        items[b_item] = cnt
        b = cnt  
        cnt += 1 
    
    graph[a].append(b)
    indegree[b] += 1 

# item_index 딕셔너리로 item index로 item이름을 찾을 수 있도록 했다. 
item_index = {v:k for k,v in items.items()}
# print(graph)
# print(indegree)

res = topology_sort(cnt)
if res==-1: 
    print(-1)
else:
    for r in res: 
        print(r)



