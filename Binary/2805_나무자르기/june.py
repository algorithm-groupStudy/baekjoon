N, G = map(int,input().split())
Tree = list(map(int,input().split()))
Tree.sort()
def bin(Tree,goal):
    start = 0
    end = len(Tree)-1
    
    while start<= end:
        mid = (start+end)//2
        ans = sum(Tree[mid:])-Tree[mid]*len(Tree[mid:])
        if ans > goal:
            start = mid+1
            check = 1
        elif ans< goal:
            end = mid-1
            check=0
        else:
            return Tree[mid]
    
    if check ==1:
        mid = mid+1
        ans =sum(Tree[mid:])-Tree[mid]*len(Tree[mid:])

    sos = Tree[mid]
    lenth = len(Tree)-mid  # lenth 씩 커진다    
    dif = goal - ans
    xy = dif % lenth
    xx = dif // lenth
    if xy==0:
        sos = sos -xx
    else:
        sos = sos-(xx+1)
    return sos

    
    
    
    
    
    
    
    # if check==1:
    #     mid = mid+1
    # ans = sum(Tree[mid:])-Tree[mid]*len(Tree[mid:])
    # sos = Tree[mid]
    
    # dif = goal-ans
    # xx = dif//(len(Tree)-mid)
    # xy = dif%(len(Tree)-mid)
    # if xy ==0:
    #     sos = sos-xx
    # else:
    #     sos = sos-xx-1
    # return sos
    
    
    
    # while ans < goal:
    #     sos -=1
    #     ans += len(Tree)-mid
    # return sos
        
        

print(bin(Tree,G))
# a = [4 ,26, 40, 42, 46, 50] 1 3 7 11      22     40 2 6 10    18
# # print(bin(a,17))
# 10 15 17 20
# 4 26 40 42 46
#                     54
# 4  46  25 ans = 16+17+21 54 ///20
# 25 46  35 ans = 5+7+11  23///20
# 35 46  40 ans = 2 + 6    8 //20 
# 35 40  37 ans = 3+5+9    17 // 20
# 35 37  36 ans = 4+6+10   20 // 20    


# 40 : 0 2 6     9  12 15 18 21
# 26 : 14 16 20  50 