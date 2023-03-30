# BOJ 9372 상근이의 여행

import sys


def dfs(start, visited, cost):
    visited[start] = 1

    for n in adjL[start]:
        if visited[n] == 0:
            cost = dfs(n, visited, cost + 1)
    return cost


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, sys.stdin.readline().split())
    adjL = [list() for _ in range(N + 1)]
    for _ in range(M):
        s, e = map(int, sys.stdin.readline().split())
        adjL[s].append(e)
        adjL[e].append(s)

    visited = [0 for _ in range(N + 1)]
    cost = dfs(1, visited, 0)
    print(cost)