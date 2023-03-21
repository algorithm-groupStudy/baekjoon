import sys
sys.stdin = open('/Users/hyunwoochoi/Desktop/python/algo/baekjoon/input.txt')
N, T = map(int, input().split())
parent = [i for i in range(N)]

def find_parent(x):
    if x != parent[x]:
        x = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
        return False
    elif x > y:
        parent[x] = y
        return False
    else:
        return True

for i in range(1, T+1):
    x, y = map(int, input(). split())
    if union_parent(find_parent(x), find_parent(y)):
        print(i)
        break
    elif i == T:
        print(0)

