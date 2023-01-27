## 시간초과 엉엉

def binary_search(goal, data):
    start = 0
    end = len(data) - 1
    count = 0
    while start <= end:
        mid = (start + end) // 2 
        if data[mid] == goal:
            mid_under =mid
            while data[mid_under]==goal:
                count = count+1
                if mid_under<=start:
                    break
                else:
                    mid_under=mid_under-1
            while data[mid]==goal:
                count = count+1
                if mid>=end:
                    break
                else:
                    mid = mid+1
            return count-1    
        if data[mid] < goal:
            start = mid + 1 
        elif data[mid] > goal:
            end = mid - 1
    return count

n = int(input()) # 5를 입력 
n_num = list(map(int,input().split()))
n_num.sort()
answer = []
m = int(input())
m_num = list(map(int,input().split()))
for ins_number in m_num: # ins_number 모두 넣어서 확인하기 
    answer.append(binary_search(ins_number, n_num))
print(' '.join(map(str,answer)))
