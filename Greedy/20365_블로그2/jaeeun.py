# BOJ 20365
# 블로그 2

N = int(input())
problems = input()

before = problems[0]
count = 1
for idx in range(1, len(problems)):
    if problems[idx] != before:
        count += 1
        before = problems[idx]

res = (count // 2) + 1
print(res)

