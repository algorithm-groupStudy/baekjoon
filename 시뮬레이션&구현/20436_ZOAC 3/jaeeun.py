# BOJ 20436 
# ZOAC 3 (구현)

# 키보드 자리에 좌표 부여 
pos_l = {'q':(0,0), 'w':(0, 1), 'e':(0,2), 'r':(0, 3), 't':(0, 4),
         'a':(1,0), 's':(1,1), 'd':(1,2), 'f':(1,3), 'g':(1,4),
         'z':(2,0), 'x':(2,1), 'c':(2,2), 'v':(2,3)}
pos_r = {'y':(0,5), 'u':(0,6), 'i':(0,7), 'o':(0,8), 'p':(0,9),
         'h':(1,5), 'j':(1,6), 'k':(1,7), 'l':(1,8),
         'b':(2,4), 'n':(2,5), 'm':(2,6)}


sl, sr = input().split()
letters = input()
secs = 0 
# 왼손, 오른손 각각에 대해 택시 거리 계산 
for l in letters: 
    if l in pos_l: 
        secs += (abs(pos_l[l][0]-pos_l[sl][0]) + abs(pos_l[l][1]-pos_l[sl][1]) + 1)
        sl = l 
    elif l in pos_r:
        secs += (abs(pos_r[l][0]-pos_r[sr][0]) + abs(pos_r[l][1]-pos_r[sr][1]) + 1)
        sr = l

print(secs)  


