import sys
sys.stdin = open("test.txt")
n = int(input())
lst = []


for i in range(n):
    pos, height = map(int, input().split())
    lst.append([pos, height])

lst.sort()

while lst:
    min_height = 1e3+1
    pos = 0
    for i in range(len(lst)):
        if min_height > lst[i][1]:
            min_height = lst[i][1]
            pos = lst[i][0]

    lst_pos_sort = sorted(lst, key=lambda x: x[0])
    lst_height_sort = sorted(lst, key=lambda x: x[1], reverse=True)
