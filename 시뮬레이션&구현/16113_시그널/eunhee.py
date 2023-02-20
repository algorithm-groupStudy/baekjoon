import sys
sys.stdin = open("text.txt")
dir = {0: ["#####", "#...#", "#####"],
       1: ["#####"], 2: ["#.###", "#.#.#", "###.#"],
       3: ["#.#.#", "#.#.#", "#####"], 4: ["###..", "..#..", "#####"],
       5: ["###.#", "#.#.#", "#.###"], 6: ["#####", "#.#.#", "#.###", ],
       7: ["#....", "#....", "#####"], 8: ["#####", "#.#.#", "#####"],
       9: ["###.#", "#.#.#", "#####"]}


def check(arr):
    for i in range(10):
        if arr == dir[i]:
            return str(i)


n = int(input())
string = input()
lst_copy = [[] for _ in range(100001)]
lst = []

for i in range(5):
    num = ""
    for j in range(i*(n//5), (i+1)*(n//5)):
        num += string[j]
    lst.append(num)

res = []
total = ""
for i in range(n//5):
    num_string = ""
    for j in range(5):
        num_string += lst[j][i]
    if num_string == ".....":
        if res:
            total += check(res)
        res.clear()
    else:
        res.append(num_string)
if res:
    total += check(res)

print(total)
