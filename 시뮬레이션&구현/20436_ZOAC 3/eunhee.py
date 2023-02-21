import sys
sys.stdin = open("test.txt")
dic_l = {"q":(0, 0), "w":(0, 1), "e":(0, 2), "r":(0, 3), "t":(0, 4), "a":(1, 0), "s":(1, 1), "d":(1, 2), "f":(1, 3),"g": (1, 4), "z":(2, 0), "x":(2, 1), "c":(2, 2), "v":(2, 3)}
dic_r = {"y":(0, 5), "u":(0, 6), "i":(0, 7), "o":(0, 8), "p":(0, 9), "h":(1, 5), "j":(1, 6), "k":(1, 7), "l":(1, 8), "b":(2, 4), "n":(2, 5), "m":(2, 6)}

    

def count_time(string):
    total_time = 0
    cur_l = s_l
    cur_r = s_r
    for s in string:
        if s in dic_l:
            pre_x, pre_y = dic_l[cur_l]
            cur_x, cur_y = dic_l[s]
            cur_l = s
            total_time += abs(pre_x-cur_x) + abs(pre_y-cur_y)
        else:
            pre_x, pre_y = dic_r[cur_r]
            cur_x, cur_y = dic_r[s]
            cur_r = s
            total_time += abs(pre_x-cur_x) + abs(pre_y-cur_y)
    return total_time
s_l, s_r = input().split()
input_string = input()
print(count_time(input_string)+len(input_string))


