import sys
sys.stdin = open(r'C:\Users\byfor\OneDrive\바탕화~1-LAPTOP-OKI97V9F-10945\git\Algo\baekjoon\시뮬레이션&구현\input.txt')

loc_qwerty = {
    'q' : (1,3),
    'w' : (2,3),
    'e' : (3,3),
    'r' : (4,3),
    't' : (5,3),
    'y' : (6,3),
    'u' : (7,3),
    'i' : (8,3),
    'o' : (9,3),
    'p' : (10,3),
    'a' : (1,2),
    's' : (2,2),
    'd' : (3,2),
    'f' : (4,2),
    'g' : (5,2),
    'h' : (6,2),
    'j' : (7,2),
    'k' : (8,2),
    'l' : (9,2),
    'z' : (1,1),
    'x' : (2,1),
    'c' : (3,1),
    'c' : (4,1),
    'v' : (5,1),
    'b' : (6,1),
    'n' : (7,1),
    'm' : (8,1),
}

loc_left, loc_right = input().split()
left_hand_x, left_hand_y = loc_qwerty.get(loc_left)
right_hand_x, right_hand_y = loc_qwerty.get(loc_right)
want_to_type = list(input())
time = 0
i = 0 
while len(want_to_type) >= i:
    des_x, des_y = loc_qwerty.get(want_to_type[i])
    ways_left = abs(des_x-left_hand_x) + abs(des_y-left_hand_y)
    ways_right = abs(des_x-right_hand_x) + abs(des_y-right_hand_y)
    if ways_left > ways_right :
        time += ways_right
        time += 1
        right_hand_x = des_x
        right_hand_y = des_y
    else:
        time += ways_left
        time += 1
        left_hand_x = des_x
        left_hand_y = des_y
    i =+ 1
print(time)

