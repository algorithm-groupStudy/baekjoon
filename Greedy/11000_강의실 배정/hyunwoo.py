import heapq

num_lectures = int(input())
lectures =[] 

for i in range(num_lectures):
    time_lecture = list(map(int, input().split()))
    lectures.append(time_lecture)

# 시작 시간으로 sort
lectures.sort(key=lambda lectures: lectures[0])
end_times = []

for lecture in lectures:
    # 강의의 시작시간이 이전강의의 종료시간 이후라면, replace
    if end_times and end_times[0] <= lecture[0]:
        heapq.heapreplace(end_times, lecture[1])
    # 강의의 시작시간이 이전 강의의 종료시간 전이라면, end_times에 추가 
    else:
        heapq.heappush(end_times, lecture[1])
    # end_times
    # [3]
    # [3, 4]
    # [4, 5]

print(len(end_times))


