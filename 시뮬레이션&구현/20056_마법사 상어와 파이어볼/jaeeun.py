# BOJ 20056
# 마법사 상어와 파이어볼
import pprint

def merge(i, j, indices, fire):
    total_mass = 0
    total_speed = 0
    initial = fire[indices[0]][4] % 2
    initial_v = True
    for index in indices:
        total_mass += fire[index][2]
        total_speed += fire[index][3]
        if fire[index][4] % 2 != initial:
            initial_v = False

    mass = total_mass // 5
    speed = total_speed // len(indices)

    if mass == 0:
        return []
    newfire = []
    for k in range(4):
        if initial_v:
            newfire.append([i, j, mass, speed, k * 2])
        else:
            newfire.append([i, j, mass, speed, k * 2 + 1])
    return newfire


N, M, K = map(int, input().split())
fire = []
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fire.append([r-1, c-1, m, s, d])

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

for k in range(K):
    tmp = [[[] for _ in range(N)] for _ in range(N)]
    tmp2 = []
    for idx, f in enumerate(fire):
        r, c, s, d = f[0], f[1], f[3], f[4]
        new_r = (r + di[d] * s) % N
        new_c = (c + dj[d] * s) % N
        tmp[new_r][new_c].append(idx)
    for i in range(N):
        for j in range(N):
            if len(tmp[i][j]) == 1:
                f_idx = tmp[i][j][0]
                tmp2.append([i, j, fire[f_idx][2], fire[f_idx][3], fire[f_idx][4]])
            if len(tmp[i][j]) >= 2:
                tmp2 += merge(i, j, tmp[i][j], fire)

    fire = tmp2

res = 0
for f in fire:
    res += f[2]

print(res)




