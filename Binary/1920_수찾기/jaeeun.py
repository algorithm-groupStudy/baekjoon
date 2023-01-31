N = int(input())
numlst = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))



def binary(num, arr):
    l, r = 0, len(arr)-1 
    while l <= r:
        mid = (l + r) // 2 
        if arr[mid] == num: 
            return 1

        elif arr[mid] < num:
            l = mid + 1 
        
        elif arr[mid] > num:
            r = mid - 1 

    return 0

numlst.sort()
for num in check:
    print(binary(num, numlst)) 
