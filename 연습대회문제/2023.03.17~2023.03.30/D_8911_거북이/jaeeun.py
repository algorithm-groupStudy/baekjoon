T = int(input())

for tc in range(1, T + 1):
    command = input()

    l = r = t = b = 0

    cx, cy = 0, 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 현재 방향
    direc = 0

    for c in command:
        if c == "F":
            cx += dx[direc]
            cy += dy[direc]
        # 현재 보고 있는 방향 반대로
        elif c == "B":
            cx -= dx[direc]
            cy -= dy[direc]
        # 방향 전환
        elif c == "L":
            direc = (direc - 1) % 4
        elif c == "R":
            direc = (direc + 1) % 4
        # 거북이가 지나간 영역의 경계 (l 왼쪽, r 오른쪽, b 아래, t 위) 업데이트
        l = min(l, cx)
        r = max(r, cx)
        b = min(b, cy)
        t = max(t, cy)

    print((r - l) * (t - b))