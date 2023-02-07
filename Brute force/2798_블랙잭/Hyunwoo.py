n, m = map(int, input().split())
num_lst = list(map(int, input().split()))
from itertools import combinations


com_lst = list(combinations(num_lst,3))
max_com = 0
for com in com_lst:
    tmp = sum(com)
    if tmp > max_com and m >= tmp :
        max_com = tmp

print(max_com)
# sum every possible combinations of sum and save it on list,
# find the close number to 'm' 
