N, M = map(int, input().split())
nums = list(map(int, input().split()))

total = 0
end = 0   
count = 0

for start in range(N): 
    while total < M and end < N:  
        total += nums[end]  # end 포인터가 가리키는 데이터를 합함 
        end += 1 
    if total == M: 
        count += 1 
    total -= nums[start] # start 포인터가 가리키는 포인터를 빼고, 한 칸 앞으로 

print(count)