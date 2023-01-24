n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))


cnt = {}
for i in a :
    if i in cnt :
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in b:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end = ' ')
        
        
"""
이 문제 이분탐색으로 푸는 효율적인 방법이 있을까요?

"""