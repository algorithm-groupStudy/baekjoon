import sys
sys.stdin = open("/Users/hyunwoochoi/Desktop/python/sample_input.txt")

num_questions = int(input())
questions = list(input())

b_cnt = 0
r_cnt = 0
tmp_list = [questions[0]]

for i in range(1, num_questions):
    if questions[i] == questions[i-1]:
        pass
    else :
        tmp_list.append(questions[i])

for idx in tmp_list:
    if idx == "B":
        b_cnt += 1
    else:
        r_cnt += 1

if b_cnt > r_cnt:
    print(r_cnt + 1 )
else:
    print(b_cnt + 1)

