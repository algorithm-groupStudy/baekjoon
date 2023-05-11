import sys

# 상근이네 집에서 한번에 festival에 도착할 수 있는지 확인,
# 가능 하다면 한번에 진입, 불가능 하다면 편의점 까지 갈 수 있는지, 갈 수 있다면 편의점에서부터
# 맥주 한 박스를 들고 출발, 한 박스에는 20개의 맥주



t = int(input())

for test_case in range(1, t+1):
    num_store = int(input())
    loc_home = list(map(int, input().split()))
    loc_store = [list(map(int, input().split())) for _ in range(num_store)]
    x, y  = map(int, input().split())
    visited = set()
    result = 'sad'
    queue = [(x,y)]

    while queue:
        # queue 값 pop
        x, y = queue.pop(0)
        # 해당 위치에서,
        if (abs(loc_home[0] - x) + abs(loc_home[1] - y)) <= 20 * 50:
            result = 'happy'
        else:
            for store in loc_store:
                store = tuple(store)
                if store not in visited and (abs(store[0] - x) + abs(store[1] - y)) <= 20 * 50:
                    visited.add(store)
                    queue.append(store)
    print(result)