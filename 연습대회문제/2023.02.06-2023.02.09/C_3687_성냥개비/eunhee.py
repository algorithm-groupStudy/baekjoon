import sys
t = int(input())

for i in range(t):
    n = int(input())
    dp_max = [0 for _ in range(101)]
    dp_min = [0 for _ in range(101)]
    dp_max[2], dp_max[3] = "1", "7"
    dp_min[2], dp_min[3], dp_min[4], dp_min[5], dp_min[6], dp_min[7], dp_min[8] = "1", "7", "4", "2", "6", "8", "10"
    min_lst = ["1", "7", "4", "2", "0", "8", "10"]
    for i in range(9, n+1):
        min_num = sys.maxsize
        string_num = ""
        for j in range(2, 8):
            string_num = dp_min[i-j]+min_lst[j-2]
            min_num = min(int(string_num), int(min_num))
            dp_min[i] = str(min_num)

    for i in range(4, n+1):
        if i % 2 == 0:
            dp_max[i] = dp_max[2]*(i//2)
        else:
            dp_max[i] = dp_max[i-2]+dp_max[2]

    print(dp_min[n], dp_max[n])
