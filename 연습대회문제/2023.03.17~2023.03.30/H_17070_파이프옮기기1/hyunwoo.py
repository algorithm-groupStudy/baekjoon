import sys
sys.stdin = open('input.txt')


size_of_map = int(input())
board = [list(map(int, input().split())) for _ in range(size_of_map)]

visited = []
def dfs(lst, loc_x, loc_y):
    # 목적지에 도착하면 리턴 
    if len(lst) == loc_x == loc_y:
        return

    if 0 =< loc_x + 1  
    