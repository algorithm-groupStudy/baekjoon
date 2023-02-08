# 1806 부분합
 

N, S = map(int, input().split())
nums = list(map(int, input().split()))

total = 0
start, end = 0, 0 
length = N + 1

# 참고 코드 
while True:
    if total >= S: 
        curr_length = end - start 
        if length > curr_length:
            length = curr_length
        total -= nums[start]
        start += 1 
    elif end == N: 
        break 
    else: 
        total += nums[end]
        end += 1 

'''
수정 이전 코드  
for start in range(N): 
    while total < S and end < N: 
        total += nums[end]
        end += 1
    if total >= S:
        curr_length = end - start
        if length > curr_length: 
            length = curr_length 
        total -= nums[start]
    if end >= N:         # elif로 바꿔서 해결 --> end가 끝까지 갔고, start가 늘어나도 여전히 totaldl S가 넘어 최소길이가 줄어드는 경우를 포함 x 
        break
'''    

if length == N + 1: 
    print(0) 
else: 
    print(length)