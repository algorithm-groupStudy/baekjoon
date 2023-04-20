# BOJ 14621 나만 안되는 연애 

# 크루스칼 알고리즘 사용 
# + 남-남, 여-여학교끼리 연결되지 않게 한다. 

import sys 
input = sys.stdin.readline

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x >= y:
        parent[x] = y
    else:
        parent[y] = x

N, M = map(int, input().split())
school = input().split()
school = ['X'] + school
edges = []
parent = [i for i in range(N+1)]
for _ in range(M):
    u, v, d = map(int, input().split())
    edges.append([d, u, v])

edges.sort()

total = 0
cnt = 0
for edge in edges:
    e, u, v = edge
    if find_parent(u) != find_parent(v):  # 이미 연결되어있는지 체크 
        if school[u] != school[v]:  # 같은 종류의 학교인지 체크 
            union(u, v)  # 합집합 
            total += e
            cnt += 1
    if cnt == N-1:
        break

if cnt < N-1:  # 다 연결하지 못했을 경우 -1을 출력 
    print(-1)
else:
    print(total)