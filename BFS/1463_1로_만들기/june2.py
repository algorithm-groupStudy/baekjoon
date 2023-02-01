from collections import deque
x = int(input())
visit = [0 for _ in range(x+1)]
queue = deque([x])

while queue:
    a = queue.popleft()
    if a==1:
        break
    if a%3==0 and visit[a//3]==0:
        queue.append(a//3)
        visit[a//3] = visit[a]+1
    if a%2==0 and visit[a//2]==0:
        queue.append(a//2)
        visit[a//2] = visit[a]+1
    if visit[a-1]==0:
        queue.append(a-1)
        visit[a-1]=visit[a]+1
print(visit)
