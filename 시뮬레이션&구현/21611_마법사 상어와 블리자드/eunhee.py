def attack(x, y, d, s):
    for _ in range(s):
        nx, ny = d_lst[d][0]+x, d_lst[d][1]+y
        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] = 0
            x, y = nx, ny


def move_ball(lst):
    move_d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    res_lst = []
    x, y = cur_x, cur_y
    range_s, range_e = x, y
    idx = 1
    change_d = 0
    while idx < n*n:
        nx, ny = x + move_d[change_d][0], y+move_d[change_d][1]
        if range_s <= nx <= range_e and range_s <= ny <= range_e:
            x, y = nx, ny
            idx += 1
            if lst[nx][ny] != 0:
                res_lst.append(lst[nx][ny])
            continue

        if x == y and x <= cur_x and y <= cur_y:
            range_s -= 1
            range_e += 1
        else:
            change_d = (change_d+1) % 4
    return res_lst


def pop_ball(lst):
    global total_cnt~
    stack = []
    flag = True
    while flag:
        f = False
        cnt = 1
        num_s = 0
        for num in lst:
            if stack and stack[-1] == num:
                cnt += 1
                num_s = num

            else:
                if cnt >= 4:
                    f = True
                    while stack and stack[-1] == num_s:
                        if num_s == 1:
                            total_cnt += 1
                        elif num_s == 2:
                            total_cnt += 2
                        else:
                            total_cnt += 3
                        stack.pop()
                cnt = 1
                num_s = 0

            stack.append(num)
        if num_s and cnt >= 4:
            while stack and stack[-1] == num_s:
                if num_s == 1:
                    total_cnt += 1
                elif num_s == 2:
                    total_cnt += 2
                else:
                    total_cnt += 3
                stack.pop()

        if f:
            lst = stack[:]
            stack.clear()
            continue
        flag = False
    return lst


def group_ball(lst):
    res = []
    num_d = 0
    cnt = 1
    while lst:
        num = lst.pop(0)
        if not num_d:
            num_d = num
            continue
        if num == num_d:
            cnt += 1
        else:
            res.append(cnt)
            res.append(num_d)
            num_d = num
            cnt = 1
    if res and res[-1] != num_d:
        res.append(cnt)
        res.append(num_d)
    res = res+[0 for _ in range(n*n-len(lst))]
    return res[:n*n]


def result(lst):
    move_d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    res_lst = [[0 for _ in range(n)] for _ in range(n)]
    x, y = cur_x, cur_y
    range_s, range_e = x, y
    idx = 0
    change_d = 0
    while idx < n*n-1:
        nx, ny = x + move_d[change_d][0], y+move_d[change_d][1]

        if range_s <= nx <= range_e and range_s <= ny <= range_e:
            res_lst[nx][ny] = lst[idx]
            x, y = nx, ny
            idx += 1
            continue

        if x == y and x <= cur_x and y <= cur_y:
            range_s -= 1
            range_e += 1
        else:
            change_d = (change_d+1) % 4
    return res_lst


total_cnt = 0
n, m = map(int, input().split())
cur_x = cur_y = n//2
board = [list(map(int, input().split())) for _ in range(n)]
d_lst = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(m):
    d, s = map(int, input().split())
    d -= 1
    attack(cur_x, cur_y, d, s)
    res = move_ball(board)

    res = pop_ball(res)
    res = group_ball(res)

    board = result(res)
    # print()
    # for row in board:
    #     print(row)
print(total_cnt)
