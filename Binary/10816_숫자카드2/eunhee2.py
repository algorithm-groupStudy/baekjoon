# 메모리114956KB 시간744ms
from collections import Counter
n=int(input())
dic = Counter(list(map(int,input().split())))
m=int(input())
person=list(map(int,input().split()))

print(*[dic[num] if num in dic else 0 for num in person])