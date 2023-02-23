dir_1 = {1: ['#', '#', '#', '#', '#']},
dirs = {
    0: ['###', '#.#', '#.#', '#.#', '###'],
    2: ['###', '..#', '###', '#..', '###'],
    3: ['###', '..#', '###', '..#', '###'],
    4: ['#.#', '#.#', '###', '..#', '..#'],
    5: ['###', '#..', '###', '..#', '###'],
    6: ['###', '#..', '###', '#.#', '###'],
    7: ['###', '..#', '..#', '..#', '..#'],
    8: ['###', '#.#', '###', '#.#', '###'],
    9: ['###', '#.#', '###', '..#', '###']
}

total_str = int(input())
signals = input()

# 한줄에 몇개씩?
str_in_line = total_str // 5

signal_array = []
for cut in range(0,total_str,str_in_line):
    tmp = signals[cut:cut+str_in_line]  # 한줄씩 잘라서
    signal_array.append(tmp)  #

# print(f'입력된 시그널 {str_in_line}')
# print(f'시그널을 각 줄로 자름 {signal_array}')

str_array = []
# 세로 줄로 하나씩 확인 할 수 있도록 함, 맨 앞에서부터 확인하기
i = 0
while str_in_line > i:
    # 세로줄이 전부 공백이라면 빈칸임 다음 숫자를 찾아라
    if i >= str_in_line:
        break
    # 세로줄이 전부 공백이라면 빈칸이므로 i + 1 을 해주고 넘어감
    elif signal_array[0][i] == '.':
        tmp = 0
        for j in range(5):
            if signal_array[j][i] == '.':
                tmp += 1
            else:
                break
        if tmp == 5:
            i += 1
            continue
    # 세로줄이 공백이 아니라면, 숫자임
    # 1 말고 다른 것 중 하나 고름
    for dir in dirs:
        tmp = 0
        # 세로 길이 확인
        for j in range(5):
            if dirs.get(dir)[j] == signal_array[j][i:i+len(dirs.get(dir)[j])]:
                tmp += 1
            else:
                break
        if tmp == 5:
            str_array.append(dir)
            i += len(dirs.get(dir)[0])
            break

    # 1인지 확인
    if i >= str_in_line:
        break
    elif signal_array[j][i] == '#':
        tmp = 0
        for j in range(5):
            if signal_array[j][i] == '#':
                tmp += 1
            else:
                break
        if tmp == 5:
            str_array.append(1)
            i += 1

result = ''.join(map(str,str_array))
print(result)