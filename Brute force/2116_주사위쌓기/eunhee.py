import sys
sys.stdin = open("test.txt")
n = int(input())
dice_lst = []

for i in range(n):
    dice = list(map(int, input().split()))
    dice_lst.append(
        [[dice[0], dice[5]], [dice[1], dice[3]], [dice[2], dice[4]]])

d = [(0, 5), (1, 3), (2, 4)]

max_total = 0
for i in range(1, 7):  # 1~7까지 경우의 수 찾기
    num = i  # 맞닿아야 되는 수
    total = 0
    for j in range(n):  # 주사위 리스트 돌기
        for k in range(3):  # 주사위 면
            if num == dice_lst[j][k][0]:  # 이거일때 다음 맞닿아야되는 면은
                num = dice_lst[j][k][1]
            elif num == dice_lst[j][k][1]:
                num = dice_lst[j][k][0]
            else:
                continue
            lst_max = dice_lst[j][k-1]+dice_lst[j][k-2]
            total += max(lst_max)
    max_total = max(total, max_total)
print(max_total)

