N = int(input())
# 5 x M 
M = N // 5
code = input()

arr = [['.' for _ in range(M)] for _ in range(5)]
idx = 0
for i in range(5):
    for j in range(M):
        arr[i][j] = code[idx]
        idx += 1

# i = 0 부터 M-1까지 체크 
res = ''
i = 0
while i < M:
    # #가 나오면 숫자 맨 앞자리라고 생각 
    if arr[0][i] == '#':
        # 맨 마지막 두 칸에 있을 경우 숫자는 1 
        if i == M-2 or i == M-1:
            res += '1'
            i += 2
            continue
        # '#.' 형태일 경우 숫자 1인지 체크 
        if arr[0][i+1] == '.':
            for j in range(1, 5):
                if arr[j][i] != '#':
                    break
            else:
                res += '1'
                i += 2
                continue
        # 위 경우가 아니면서 '#.#'이면 4 
        if arr[0][i+1] == '.' and arr[0][i+2] == '#':
            res += '4'
            # 숫자는 총 3칸 차지, 숫자 사이 1열 공백 있으므로 인덱스에 +4 해줌 
            i += 4
            continue
        # 4가 아니면서 아래 조건 만족하면 7 
        if arr[4][i] == '.':
            res += '7'
            i += 4
            continue
        if arr[2][i+1] == '.':
            res += '0'
            i += 4
            continue
        if arr[1][i] == '#':
            if arr[1][i+2] == '#':
                if arr[3][i] == '#':
                    res += '8'
                    i += 4
                else:
                    res += '9'
                    i += 4
            else:
                if arr[3][i] == '#':
                    res += '6'
                    i += 4
                else:
                    res += '5'
                    i += 4
        else:
            if arr[3][i] == '#':
                res += '2'
                i += 4
            else:
                res += '3'
                i += 4
    # 공백이면 한 칸 증가 
    else:
        i += 1

print(res)