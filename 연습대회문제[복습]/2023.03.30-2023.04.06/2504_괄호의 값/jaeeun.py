# BOJ 2504 괄호의 값

def check_paren(paren):
    # level: 괄호가 현재 몇 번 중첩되었는지 트래킹해준다.
    level = 0
    # 여는 괄호를 저장할 stack
    stack = []
    # cal: 각 레벨 별 계산 결과를 저장
    cal = [0] * len(paren)
    check = {')': '(', ']': '['}
    for p in paren:
        if p == '(':
            stack.append(p)
            level += 1
        elif p == '[':
            stack.append(p)
            level += 1
        elif p == ')':
            # 괄호 유효성 검사
            if stack and check[p] == stack.pop():
                # 괄호 내부에 내용이 있었을 경우 그 값에 2를 곱해줌
                if cal[level]:
                    cal[level-1] += cal[level] * 2
                # 없었을 경우 해당 레벨 괄호 값은 2가 된다.
                else:
                    cal[level-1] += 2
                cal[level] = 0
                level -= 1
            else:
                return 0
        elif p == ']':
            # 괄호 유효성 검사
            if stack and check[p] == stack.pop():
                if cal[level]:
                    cal[level-1] += cal[level] * 3
                else:
                    cal[level-1] += 3
                cal[level] = 0
                level -= 1
            else:
                return 0

    if stack:
        return 0
    else:
        return cal[0]


paren = input()
print(check_paren(paren))

#### 예전 코드 ###

parens = input()
stack = []
score = [0] * 30
prev_level = level = -1
pairs = {']': '[', ')' : '('}
table = {']': 3, ')': 2}
res = 1

for p in parens:
    if p == '(' or p == '[':
        level += 1
        stack.append(p)
    elif p == ')' or p == ']':
        if not stack or stack[-1] != pairs.get(p):
            res = 0
            break
        else:
            stack.pop()
            if level > prev_level:
                score[level] = table[p]
            elif level == prev_level:
                score[level] += table[p]
            else:
                score[level] += score[prev_level] * table[p]
                score[prev_level] = 0
            prev_level = level
            level -= 1

if stack:
    res = 0

if not res:
    print(res)

else:
    print(score[0])