N = int(input())
nums = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

num_dict = {}

for n in nums:
    if n not in num_dict:
        num_dict[n] = 1
    else:
        num_dict[n] += 1

for f in find:
    if f in num_dict:
        print(1)
    else:
        print(0)