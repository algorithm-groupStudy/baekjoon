# BOJ 1541 잃어버린 괄호
# 처음 '-' 기호가 나온 이후로 모두 뺄셈이 되도록 괄호를 적용하는 것이 식을 최소로 만드는 방법이다.
eq = input()

tmp = ''
sign = 1
total = 0
for w in eq:
    # tmp에 수를 저장한다.
    if w.isnumeric():
        tmp += w

    else:
        total += int(tmp) * sign
        tmp = ''
        # 마이너스 기호가 나온 이후로는 -1을 곱해서 total에 더해준다.
        if w == '-':
            sign = -1

total += int(tmp) * sign

print(total)