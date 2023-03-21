import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

num_people = int(input())
graph = [[] for _ in range(num_people + 1)]
fir_people, sec_people = map(int,input().split())

num_rel = int(input())
for _ in range(num_rel):
    people1, people2 = map(int, input().split())
    graph[people1].append(people2)
    graph[people2].append(people1)

visit = [0]*(num_people+1)

def dfs(start):
    for n in graph[start]:
        if visit[n] == 0:
            visit[n] = visit[start]+1 
            dfs(n)
dfs(fir_people)
print(visit[sec_people] if visit[sec_people] > 0 else -1)


               
