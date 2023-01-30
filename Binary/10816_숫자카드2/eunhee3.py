def BSearchRecursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return BSearchRecursive(arr, target, low, mid-1)
    else:
        return BSearchRecursive(arr, target, mid+1, high)


BSearchRecursive([1,2,3,4,5,6,10,11],10,0,7)


