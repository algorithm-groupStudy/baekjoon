# 나중에 다시 풀기
import sys
sys.stdin=open("test.txt")


def bf(start):
  spend[start]=0
  for i in range(N):
    for j in range(len(path)):
      cur = path[j][0]
      to = path[j][1]
      cost = path[j][2]
      if spend[to] > spend[cur] + cost:
        spend[to] = spend[cur]+cost
        if i==N-1:
          return True
  return False


T = int(input())


for tc in range(T):
  INF = 1e9
  path = []
  N,M,W = map(int,input().split())
  spend = [INF for _ in range(N+1)]
  for _ in range(M):
    S,E,T = map(int,input().split())
    path.append((S,E,T))
    path.append((E,S,T))
  for _ in range(W):
    S,E,T = map(int,input().split())    #줄어드는 시간
    path.append((S,E,-T))
  bf_solve = bf(1)
  print(spend)

  if bf_solve:
    print("YES")
  else:
    print("NO")