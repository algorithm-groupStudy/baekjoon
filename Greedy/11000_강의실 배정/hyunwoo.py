import sys
sys.stdin = open("/Users/hyunwoochoi/Desktop/python/sample_input.txt")

num_lectures = int(input())

lectures =[] 
for i in range(num_lectures):
    time_lecture = list(map(int, input().split()))
    lectures.append(time_lecture)
lectures = sorted(lectures, key = lambda lecture: lectures[0])
lectures = sorted(lectures, key = lambda lecutre: lectures[1])
print(lectures)
print(lectures[0])
print(lectures[0][0])
last = 0
i = 0
cnt = 1
while lectures:
    if lectures[i][0] > last :
        last = lectures[i][1]
        lectures.remove(lectures[i])
        continue
    elif i == len(lectures):
        last = 0
        i = 0
        cnt += 1
    else:
        i += 1


print(lectures)
    


