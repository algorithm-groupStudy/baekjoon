num_tree, need_tree = map(int, input().split())
lst_tree = list(map(int, input().split()))
lst_tree.sort()

def lower_bound (arr, x):
    l, r = 0, len(arr)-1
    res = -1
    while l <= r:
        m = (l+r) // 2 
        
        if x <= arr[m]:
            res = m
            r = m - 1
        else:
            l = m + 1
    return res




# tree 들을 자른 값 
for tree in num_tree:
    
    
'''
높이의 최댓값 구하기 
제일 긴 놈, 과 제일 작은 놈의 중간 값을 구하고, 
중간값으로 잘랐을때, 나무의 길이 가 목표길이보다 큰지 작은지
목표길이보다 크다면, 가장 긴 길이와 중간값의 중간을 구해서 다시 자르기 

'''