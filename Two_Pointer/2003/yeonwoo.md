```python
#############완전 탐색 함수 정의 시작####################
def getSum(j, i, arr):
    sum = 0

    idx = j
    while (j <= i):
        sum += arr[j]
        j += 1
    return sum
def exhaustiveSearch(n, m, arr):
    result = 0
    for i in range(n):
        # print(f'i={i}')
        for j in range(0, i + 1):
            # print(f'\tj={j}')
            sum = getSum(j, i, arr)
            if sum == m:
                result += 1
    return result

#############완전 탐색 함수 정의 종료######################


#############투 포인터 함수 정의 시작######################
def twoPointer(n,m,arr):
    result = 0

    front = 0
    back = 0
    sumVal = arr[0]

    while back<n:
        if sumVal==m:#찾았으면
            # print(f'{front} , {back} ->{result}')
            result += 1 #결과반영

            back += 1
            if back>=n:
                break
            sumVal += arr[back]

        elif sumVal<m: #sum값이 m보다 작으면 범위 증가
            back += 1
            if back>=n:
                break
            sumVal += arr[back]


        else: #sum값이 m보다 크면 범위 감소
            sumVal -= arr[front]
            front += 1

            if front > back:
                back += 1
                if back >= n:
                    break
                sumVal += arr[back]
    return result
#############투 포인터 함수 정의 종료######################



#######################인풋 받는 공간############################
n, m = map(int, input().split())
arr = list(map(int, input().split()))
#######################인풋 받는 공간 종료########################

##############문제 푸는 공간 시작 ##############
# print(exhaustiveSearch(n,m,arr))
print(twoPointer(n,m,arr))
##############문제 푸는 공간 종료 ##############
```

