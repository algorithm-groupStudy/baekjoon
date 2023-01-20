import queue

T = int(input())  # 테스트 케이스


# arr 체크
def printmap(field):
    print()
    for i in range(len(field)):
        for j in range(len(field[0])):
            print(field[i][j], end=' ')
        print()


def bfs(sr, sc, field, visited, dr, dc, row_max, col_max):
    result = 0  # 영역 추가

    # 큐에 sr, sc 삽입
    q = queue.Queue()
    q.put([sr, sc])

    turn = 0
    # 큐 빌 때까지 while
    while (not q.empty()):
        # 턴 추가
        turn += 1
        # 큐사이즈 책정
        size = q.qsize()
        # 큐 사이즈만큼 루프
        while (size >= 1):
            size -= 1
            # cr, cc 찾기
            cur = q.get()
            result += 1
            cr = cur[0]
            cc = cur[1]

            for i in range(4):
                # nr, nc 책정
                nr = cr + dr[i]
                nc = cc + dc[i]

                # nr, nc 기본검증(방문, 범위)
                if (nr < 0 or nr >= row_max or nc < 0 or nc >= col_max):
                    continue  # 범위
                # print("nr=",nr,"nc=",nc)
                if (visited[nr][nc]):
                    continue  # 방문

                # field[nr][nc] 검증 (배추있는지)
                if field[nr][nc] == 1:
                    # 방문처리
                    visited[nr][nc] = True
                    # 큐에 삽입
                    q.put([nr, nc])

    # print("result",result)
    return result


dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for test_case in range(1, T+1):
    result = 0
    # 테스트 시작
    m, n, k = map(int, input().split())  # 가로, 세로, 배추
    field = [[0 for cols in range(m)] for rows in range(n)]  # 밭
    visited = [[False for cols in range(m)] for rows in range(n)]

    # 배추심기
    for i in range(k):
        c, r = map(int, input().split())  # col, row
        field[r][c] = 1

    # printmap(field)
    for i in range(len(field)):  # 행 순회
        for j in range(len(field[0])):  # 열 순회
            if not visited[i][j] and field[i][j] == 1:  # 방문체크, 배추체크
                visited[i][j] = True  # 방문처리
                area = bfs(i, j, field, visited, dr, dc, n, m)  # bfs
                result += 1  # 배추zone++
    print(result)
