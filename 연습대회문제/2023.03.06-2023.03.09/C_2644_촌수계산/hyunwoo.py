import sys
input = sys.stdin.readline

num_people = int(input())
graph = [[] for _ in range(num_people + 1)]
fir_people, sec_people = map(int,input().split())

num_rel = int(input())
for _ in range(num_rel):
    people1, people2 = map(int, input().split())
    graph[people1].append(people2)
    graph[people2].append(people1)


cnt = 0
def dfs(graph, start, end):
    global cnt
    queue = [start]
    visited = []  
    if start == end:
        return cnt
    while queue:
        tmp = queue.pop()
        if tmp not in visited :
            visited.append(tmp)
            cnt += 1
            for idx in graph[tmp]:
                if idx not in visited:
                    dfs(graph,idx,end)
        else:
            cnt = -1
            break
    return cnt 
print(dfs(graph,fir_people,sec_people))


                
                        