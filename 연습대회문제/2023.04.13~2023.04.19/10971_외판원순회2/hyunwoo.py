import sys
sys.stdin = open('input.txt')
num_city = int(input())
graph = [list(map(int, input().split())) for _ in range(num_city)]
visited = set()
result = float('inf')

def dfs(start, now, tmp, visited):
    global result, num_city
    
    # end condition 
    if len(visited) == num_city:
        if graph[now][start]:
            tmp += graph[now][start]
            if result > tmp:
                result = tmp
            return
        
    # backtracking 
    if tmp > result:
        return
    
    for i in range(num_city):
        if i not in visited and graph[now][i]:
            visited.add(i)
            dfs(start, i, tmp + graph[now][i], visited)
            visited.remove(i)

for i in range(num_city):
    visited.add(i)
    dfs(i, i, 0, visited)
    visited.remove(i)
    
print(result)
            