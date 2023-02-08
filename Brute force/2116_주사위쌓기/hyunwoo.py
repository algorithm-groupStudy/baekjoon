t = int(input().strip())  # input number of dice

#  ax = [0, 1, 2, 3, 4, 5]

# input start, return top 
def dice_stack(start_num, dice_lst):
    dice = [1, 2, 3, 4, 5, 6]
    ay = [5, 3, 4, 1, 2, 0]

    start_index = dice_lst.index(start_num)
    end = ay[start_index]
    end_num = dice_lst[end]

    dice.remove(start_num)
    dice.remove(end_num)
    max_dice = max(dice)

    # if start is a position of ax, return ay
    return end_num, max_dice


dice_lst = []
for i in range(t):
    dice_lst.append(list(map(int, input().strip().split())))

sum_list = []
for i in range(1, 7):
    sum_stack = 0
    a, tmp_stack = dice_stack(i, dice_lst[0])
    sum_stack += tmp_stack
    for j in range(1, t):
        b, tmp_stack = dice_stack(a, dice_lst[j])
        sum_stack += tmp_stack
        a = b
    sum_list.append(sum_stack)
    
print(max(sum_list))