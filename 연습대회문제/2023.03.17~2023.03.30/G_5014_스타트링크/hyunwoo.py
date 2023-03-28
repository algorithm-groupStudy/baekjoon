import sys
sys.stdin = open('input.txt')

building_stairs, current_loc, loc_start, up, down = map(int, input().split())

count = 0

while True:
    
    # 스타트 링크가 up보다 위에 있을때는 up 한다.
    if up != 0 and (loc_start - current_loc) // up > 0:
        up_botton = (loc_start - current_loc) // up
        count += up_botton
        current_loc = current_loc + (up * up_botton)
    
        if current_loc == loc_start:
            break    

    # 스타트 링크가 아래에 있고, down 보다 작을때 
    if down != 0 and (current_loc - loc_start) // down > 0:
        down_botton = (current_loc - loc_start) // down 
        count += down_botton
        current_loc = current_loc + (down* down_botton)

        if current_loc == loc_start:
            break
    
    # 스타트 링크가 
    if abs(current_loc - loc_start) % abs(up-down) == 0:
        double_botton = abs(current_loc-loc_start) // abs(up-down) 
        count += double_botton * 2
        break

    count = -1
    break

if count == -1:
    print("use the stairs")
else:
    print(count)