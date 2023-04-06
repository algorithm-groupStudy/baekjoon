# BOJ 12015 가장 긴 증가하는 부분 수열2
# 코드 참조
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]


def binary(e):  # LIS 내 위치를 찾아줘서 원소 바꿈
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start + end) // 2

        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1

    return start


for item in A:
    if LIS[-1] < item:
        LIS.append(item)  # item이 LIS 마지막 원소보다 크면 수열 연장
    else:
        idx = binary(item)
        LIS[idx] = item  # 마지막 원소가 대치되는 경우 원래보다 작은 것으로 바뀌게 된다,

print(len(LIS))
