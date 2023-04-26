import sys
sys.stdin = open("test.txt")
from collections import deque



def topology_sort():
    global q
    result = []
    q = deque()
    
    for key in input_int:
        if input_int[key]==0:
            q.append(key)
    # q=deque(sorted(q))

    while q:
        x = q.popleft()
        result.append(x)
        if x in graph:
            # lst = []
            for i in graph[x]:
                input_int[i]-=1
                if input_int[i]==0:
                    # lst.append(i)
                    q.append(i)
        print("x:",x)
        print("q:",q)
    if result:
        for i in result:
            print(i)
    else:
        print(-1)
N = int(input())
input_int = dict()
graph = dict()

for _ in range(N):
    A,B = input().split()
    if B in input_int:
        input_int[B]+=1
    else:
        input_int[B]=1
    if A in graph:
        graph[A].append(B)
    else:
        graph[A] = [B]
        if A not in input_int:
            input_int[A]=0

topology_sort()