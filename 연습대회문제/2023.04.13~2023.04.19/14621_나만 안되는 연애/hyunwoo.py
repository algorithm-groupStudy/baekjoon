def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
gender = list(input().split())
parent = [i for i in range(n + 1)]
path_sum = 0
path_num = 0

edges = []

for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b) and gender[a - 1] != gender[b - 1]:
        union_parent(a, b)
        path_sum += cost
        path_num += 1 

if path_num == n - 1:
    print(path_sum)
else:
    print(-1)