import sys
sys.stdin = open("text.txt")
# 0 부터 1까지, 세로로 봤을때 표시
dir = {0: ["#####", "#...#", "#####"],
       1: ["#####"], 2: ["#.###", "#.#.#", "###.#"],
       3: ["#.#.#", "#.#.#", "#####"], 4: ["###..", "..#..", "#####"],
       5: ["###.#", "#.#.#", "#.###"], 6: ["#####", "#.#.#", "#.###", ],
       7: ["#....", "#....", "#####"], 8: ["#####", "#.#.#", "#####"],
       9: ["###.#", "#.#.#", "#####"]}


def check(arr):    # dir중 똑같은 리스트가 있는지 확인
    for i in range(10):
        if arr == dir[i]:
            return str(i)


n = int(input())
string = input()
lst = []    

for i in range(5):    # 5개로 나눠서 담아줌
    num = ""
    for j in range(i*(n//5), (i+1)*(n//5)):
        num += string[j]
    lst.append(num)

res = []
total = ""
for i in range(n//5):    # 세로로 탐색
    num_string = ""
    for j in range(5):
        num_string += lst[j][i]
    if num_string == ".....":    # 공백일 경우
        if res:
            total += check(res)    # dir중 같은것 출력
        res.clear()    # 리스트 초기화
    else:
        res.append(num_string)  
if res:
    total += check(res)

print(total)
