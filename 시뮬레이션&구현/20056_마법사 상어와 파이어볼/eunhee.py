n, m, k = map(int, input().split())    # n*n크기, m개의줄에 파이어 정보, k번 명령
d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
lst = [[[] for _ in range(n)] for _ in range(n)]  # [0,0,0] mi, di, si
fire_lst = []


def res(arr):
    total = 0
    for m in arr:
        total += m[2]
    return total


def fire_cal(x, y):
    t_mi = 0
    t_si = 0
    t_di_odd = 0
    t_di_even = 0
    t_di = []
    for i in range(len(lst[x][y])):
        t_mi += lst[x][y][i][0]
        t_si += lst[x][y][i][1]
        if lst[x][y][i][2] % 2:
            t_di_odd += 1
        else:
            t_di_even += 1
    t_mi //= 5
    t_si //= len(lst[x][y])
    if t_di_odd == len(lst[x][y]) or t_di_even == len(lst[x][y]):
        t_di = [0, 2, 4, 6]
        # 0,2,4,6
    else:
        t_di = [1, 3, 5, 7]
        # 1,3,5,7
    return t_mi, t_si, t_di


def fire():
    for i in range(n):
        for j in range(n):
            if len(lst[i][j]) >= 2:
                t_mi, t_si, t_di = fire_cal(i, j)
                lst[i][j].clear()
                if t_mi:
                    for direction in t_di:
                        fire_lst.append([i, j, t_mi, t_si, direction])
            elif len(lst[i][j]) == 1:
                m, s, d = lst[i][j].pop()
                fire_lst.append(
                    [i, j, m, s, d])


def fireball_move(ri, ci, mi, si, di):
    nx, ny = (d[di][0]*si+ri) % n, (d[di][1]*si+ci) % n
    lst[nx][ny].append((mi, si, di))


for _ in range(m):
    # (ri, ci)파이어볼 위치, mi: 질량, si:속력, di:방향
    ri, ci, mi, si, di = map(int, input().split())
    fire_lst.append([ri-1, ci-1, mi, si, di])

for i in range(k):
    while fire_lst:
        ri, ci, mi, si, di = fire_lst.pop(0)
        fireball_move(ri, ci, mi, si, di)
    fire()

print(res(fire_lst))
