import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

nodes= int(input())
tree = [[]  for _ in range(nodes+1)]
for i in range(nodes-1):
    left_edge, right_edge = map(int, input().split())
    tree[left_edge].append(right_edge)
    tree[right_edge].append(left_edge)
    
    
visited = [0]*(nodes+1)    

def dfs(start):
    # start에서 갈 수 있는 노드들
    for i in tree[start]:
        # visited[노드]가 0으로 표시됨 : 노드의 부모 미표시 
        if visited[i] == 0:
            # visited[노드] = 부모(출발)표시 
            visited[i] = start
            dfs(i)
dfs(1)

for node in range(2,nodes+1):
    print(visited[node])    