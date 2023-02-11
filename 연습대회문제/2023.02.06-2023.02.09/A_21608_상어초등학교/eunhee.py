import sys
sys.stdin = open("test.txt")


def check_round_likes(x):  # 주변에 좋아하는 사람이 있는지 확인, x:학생번호
    max_cnt = -1
    pos_x, pos_y = -1, -1
    for i in range(n):
        for j in range(n):
            cnt = 0
            for dx, dy in d:
                nx, ny = i+dx, j+dy
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] in lst[x]:
                        cnt += (n**2)
                    elif board[nx][ny] == 0:
                        cnt += 1
            if cnt > max_cnt and board[i][j] == 0:
                max_cnt = cnt
                pos_x, pos_y = i, j

    return (pos_x, pos_y)


def happy(board):
    total = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            for dx, dy in d:
                nx, ny = i+dx, j+dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in lst[board[i][j]]:
                    cnt += 1
            if cnt == 2:
                cnt = 10
            elif cnt == 3:
                cnt = 100
            elif cnt == 4:
                cnt = 1000
            total += cnt
    return total


n = int(input())
lst = [[] for _ in range((n**2)+1)]
board = [[0 for _ in range(n)] for _ in range(n)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]


for i in range(n**2):
    stu, *likes = map(int, input().split())
    for s in likes:
        lst[stu].append(s)
    pos_x, pos_y = check_round_likes(stu)
    board[pos_x][pos_y] = stu
    res = happy(board)
print(res)
