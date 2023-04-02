import sys
sys.stdin = open('input.txt')

import heapq
# number of customers, number of counters
N, K = map(int, input().split())

cus = []
items = [] 
for customer in range(N):
    num_cus, num_item = map(int, input().split())
    cus.append(num_cus)
    items.append(num_item)
    
counter = []
for i in range(K):
    heapq.heappush(counter, (0,i))
# print(counter)

time_needed = [0] * K

finished = []
for i in range(N):
    t, x = heapq.heappop(counter)  # time needed to process the current customer and the index of computer 
    time_needed[x] += items[i]  # updates the total time needed by the counter 'x' 
    heapq.heappush(counter, (time_needed[x], x))  # then it pushes back the time_needed[x] and counter'x'
    finished.append((time_needed[x], -x, i))  # append 3 ele in finished list, timed_needed[x], negative index, num_cus

# print(finished)
# [(4, 0, 0), (5, -1, 1), (14, -2, 2), (5, 0, 3), (12, 0, 4), (10, -1, 5), (17, -1, 6), (17, 0, 7), (24, -2, 8), (20, 0, 9)]
# print(sorted(finished))
# print(enumerate(sorted(finished)))

print(sum(cus[t[2]] * (i+1) for i, t in enumerate(sorted(finished))))

# make sorted with finished, 

    
    