N, M = map(int, input().split())

list_A = list(map(int, input().split()))
list_B = list(map(int, input().split())) 

final_list = [] 
p1, p2 = 0, 0

while True:
    if list_A[p1] <= list_B[p2]:
        final_list.append(list_A[p1])
        p1 += 1
    else:
        final_list.append(list_B[p2])
        p2 += 1 
    
    if p1 == len(list_A):
        final_list.extend(list_B[p2:])
        break 
    if p2 == len(list_B):
        final_list.extend(list_A[p1:])
        break 

print(*final_list)