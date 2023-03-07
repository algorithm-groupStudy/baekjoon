# 다시 풀꺼야 
# 하 우 상 좌
dr = (0, 1, 0, -1, 0)
dc = (0, 0, 1, 0, -1)

# 0, 상, 하, 좌, 우
bli_rc = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]



# 일렬 리스트 만들기
def make_one_list():
    current_r = (N // 2) + 1
    current_c = (N // 2) + 1
    move_num = 2
    while current_c > 0:
        for i in range(1, 5):
            for j in range(move_num):
                # 처음엔 왼쪽으로 이동
                if i == 1 and j == 0:
                    current_c -= 1
                else:
                    current_r += dr[i]
                    current_c += dc[i]
                one_list.append(blocks[current_r][current_c])
        move_num += 2

        if blocks[current_r][current_c + dc[i]] == 0:
            break
    return


# blizrd 마법 이후 블록 재배치
def make_blocks():
    for i in range(N + 1):
        for j in range(N + 1):
            blocks[i][j] = 0

    current_r = (N // 2) + 1
    current_c = (N // 2) + 1
    move_num = 2
    one_list_idx = 0
    length = len(one_list)
    while current_c > 0:
        for i in range(1, 5):
            for j in range(move_num):
                # 처음엔 왼쪽으로 이동
                if i == 1 and j == 0:
                    current_c -= 1
                else:
                    current_r += dr[i]
                    current_c += dc[i]
                if length <= one_list_idx:
                    return
                while one_list[one_list_idx] == 0:
                    one_list_idx += 1
                    if length <= one_list_idx:
                        return
                blocks[current_r][current_c] = one_list[one_list_idx]
                one_list_idx += 1 
        move_num += 2
    return


# 4개 연속이면 터뜨리기
def pop_one_list():
    global one_list
    new_one_list = list()
    bomb_check = 0
    cnt = 1
    temp = -1
    for i in range(len(one_list)):
        if one_list[i] != temp:
            temp = one_list[i]
            if cnt >= 4:
                bomb_check = 1
                bomb_num[new_one_list[-1]] += cnt
                for _ in range(cnt):
                    new_one_list.pop()
            cnt = 0
        new_one_list.append(one_list[i])
        cnt += 1
    if cnt >= 4:
        bomb_check = 1
        bomb_num[new_one_list[-1]] += cnt
        for _ in range(cnt):
            new_one_list.pop()
    one_list = new_one_list[:]
    return bomb_check


# 구슬 변화(갯수, 번호)
def evolution():
    global blocks
    current_r = (N // 2) + 1
    current_c = (N // 2) + 1
    move_num = 2
    cnt = 0
    bf_num = blocks[current_r][current_c - 1]
    flag = 0
    while current_c > 0:
        for i in range(1, 5):
            for j in range(move_num):
                # 처음엔 왼쪽으로 이동
                if i == 1 and j == 0:
                    current_c -= 1
                else:
                    current_r += dr[i]
                    current_c += dc[i]

                if current_c <= 0 or current_r > N or blocks[current_r][current_c] == 0:
                    flag = 1
                    break

                # 전후 숫자가 달라지면 visited 초기화 가능
                if blocks[current_r][current_c] == bf_num:
                    cnt += 1
                elif blocks[current_r][current_c] != 0:
                    evo_list.append(cnt)
                    evo_list.append(bf_num)
                    cnt = 1
                    bf_num = blocks[current_r][current_c]
                else:
                    break
            if flag == 1:
                break
        if flag == 1:
            break
        move_num += 2


    evo_list.append(cnt)
    evo_list.append(bf_num)
    

    # 블록 재배치
    new_blocks = [[0] * (N + 1) for _ in range(N + 1)]

    current_r = (N // 2) + 1
    current_c = (N // 2) + 1
    move_num = 2
    evo_list_idx = 0
    length = len(evo_list)
    while current_c > 0:
        for i in range(1, 5):
            for j in range(move_num):
                # 처음엔 왼쪽으로 이동
                if i == 1 and j == 0:
                    current_c -= 1
                else:
                    current_r += dr[i]
                    current_c += dc[i]
                if length <= evo_list_idx:
                    break
                if current_r <= 0 or current_c <= 0:
                    blocks = new_blocks[:]
                    return
                new_blocks[current_r][current_c] = evo_list[evo_list_idx]
                evo_list_idx += 1
        move_num += 2
    blocks = new_blocks[:]
    return


N, M = map(int, input().split())
blocks = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
one_list = list()
move_list = list()
bomb_num = [0, 0, 0, 0]
for _ in range(M):
    temp_r, temp_c = map(int, input().split())
    move_list.append([temp_r, temp_c])

for blizard_d, blizard_s in move_list:
    # blizard 마법
    current_r = (N // 2) + 1
    current_c = (N // 2) + 1
    for _ in range(blizard_s):
        current_r += bli_rc[blizard_d][0]
        current_c += bli_rc[blizard_d][1]
        blocks[current_r][current_c] = 0

    one_list = list()
    # blizard 마법 이후 일렬 리스트로 붙이기
    make_one_list()

    # blizard 마법 이후 블록 재배치
    make_blocks()

    one_list = list()
    # 일렬 리스트 만들기
    make_one_list()

    again = 1
    while again:
        # 4개 연속이면 터뜨리기
        again = pop_one_list()

    # 블록 재배치
    make_blocks()

    evo_list = list()
    # 구슬 변화(갯수, 번호)
    evolution()

ans = 0
for i in range(1, 4):
    ans += bomb_num[i] * i

print(ans)