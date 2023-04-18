import sys
sys.stdin = open("test.txt")
from collections import deque
# 문제 접근법
# 1) 줄 세우기
# 2) 순서가 있다
# 3) 답이 여러개일 가능성이 있다.

def topology_sort():
    q=deque([])
    res = []
    for i in range(1,N+1):
      if indegree[i]==0:
        q.append(i)
    while q:
      x = q.popleft()
      res.append(x)
      for j in graph[x]:
          indegree[j]-=1
          if indegree[j]==0:
             q.append(j)
    print(*res)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1
topology_sort()

        