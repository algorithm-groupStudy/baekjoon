def binary_search(target,data):
    cnt = 0 # 상근이가 가지고 있는 카드 숫자
    cnt_lst = [] # 상근이가 가지고 있는 카드 갯수 구분 
    data.sort()
    start, end = 0, len(data) - 1
    while start <= end:
        mid = (start+end) // 2
        if target == data(mid):
            cnt_lst.append(data(mid))
        elif target > data(mid):
            
            
    

M = int(input())
M_list = list(map(int, input().split()))
N = int(input())
N_list = list(map(int, input().split()))

