import sys
sys.stdin = open("test.txt")


def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,x,y):
    x = find(parent,x)
    y = find(parent,y)
    if x>y:
        parent[x]=y
    else:
        parent[y]=x
N,M = map(int,input().split())
sex = list(input().split())
distance =[]
for _ in range(M):
    u,v,d = map(int,input().split())
    if sex[u-1]==sex[v-1]:
        continue
    distance.append((d,u,v))

res = 0
distance.sort()
parent = list(range(N+1))
for i in range(len(distance)):
    node1 = distance[i][1]
    node2 = distance[i][2]
    if find(parent,distance[i][1]) != find(parent,distance[i][2]):
        res+=distance[i][0]
        union(parent,node1,node2)
        
for i in range(1,len(parent)):
    parent[i] = find(parent,parent[i])
    if parent[i]!=1:
        res=0
        break
if res==0:
    print(-1)
else:
    print(res)

