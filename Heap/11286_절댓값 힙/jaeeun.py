# BOJ 11286 절댓값 힙 

import sys 
import heapq 

N = int(input())
# 양수, 음수를 저장하는 최소힙을 따로 만든다. 
q_pos = [] 
q_neg = [] 

for _ in range(N): 
    num = int(sys.stdin.readline().rstrip())
    if num > 0: 
        heapq.heappush(q_pos, num)
    # 음수의 경우 -1을 곱하여 양수로 만들어 저장한다. 
    elif num < 0: 
        heapq.heappush(q_neg, -num)
    else:
        # 두 힙이 둘 다 비어있지 않은 경우  
        if q_pos and q_neg:
            # 둘 다 pop을 하고  
            pos = heapq.heappop(q_pos)
            neg = heapq.heappop(q_neg)
            # 절댓값이 더 작은 것을 출력한다. 
            # 절댓값이 같을 경우 값이 더 작은 음수를 출력한다. 
            # 음수의 경우 -1을 다시 곱해서 출력한다. 
            # 출력하지 않은 수는 다시 heappush한다. 
            if neg <= pos:
                heapq.heappush(q_pos, pos) 
                print(-neg)
            else:
                heapq.heappush(q_neg, neg)
                print(pos)
        # 둘 중 하나만 비어있지 않을 경우 해당 힙에서 pop해 출력한다. 
        elif q_pos:
            pos = heapq.heappop(q_pos)
            print(pos)
        elif q_neg:
            neg = heapq.heappop(q_neg)
            print(-neg)
        # 둘 다 비어있을 경우 0을 출력한다. 
        else:
            print(0)