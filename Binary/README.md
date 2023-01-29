# Binary란?
Binary Search란, 결정문제의 답이 이분법적일 때 사용하는 탐색 기법

탈출 조건에 대한 고민
1) lo < hi 
2) 정답 lo or hi 
3) while 문이 끊기지 않아 시간초과

방법
1) 재귀
2) WHILE문 활용

# 발표주제 
1. 10816번을 Binary로 푸는 방법에 대해 같이 고민해요. 


    해당 문제는 백준의 단계별 문제에 이분탐색 문제로 소개되어 있으나,
저는 Dictionary를 활용해서 푸는 것이 더 효율적이라고 생각했는데 혹시 이분 탐색으로 푸는 더 효율적인 방법을 아시는분? 

2.  이 풀이는 왜 시간초과가 날까요? 한번 맞춰주세요!
``` 
def binary_search(goal, data):
    start = 0
    data.sort()
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

m = int(input())
m_num = list(map(int,input().split()))

for ins_number in m_num: # ins_number 모두 넣어서 확인하기 
    if binary_search(ins_number, n_num):
        print(1)
    else:
        print(0)


```

## bisect - 배열 이진 분할 알고리즘
