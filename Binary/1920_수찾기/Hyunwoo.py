def binary_search(goal, data):
    start = 0
    end = len(data) - 1
    
    while start <= end:
        mid = (start + end) // 2 
        if data[mid] == goal:
            return True
        
        if data[mid] < goal:
            start = mid + 1 
        elif data[mid] > goal:
            end = mid - 1

n = int(input()) # 5를 입력 
n_num = list(map(int,input().split()))
n_num.sort()

m = int(input())
m_num = list(map(int,input().split()))

for ins_number in m_num: # ins_number 모두 넣어서 확인하기 
    if binary_search(ins_number, n_num):
        print(1)
    else:
        print(0)



    
