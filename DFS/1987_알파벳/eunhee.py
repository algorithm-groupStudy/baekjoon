def dfs(x, y, cnt):
    global res, t
    res = max(res, cnt)

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < r and 0 <= ny < c and alpha_lst[nx][ny] not in lst:
            lst.add(alpha_lst[nx][ny])
            dfs(nx, ny, cnt+1)
            lst.remove(alpha_lst[nx][ny])    
            # for dx,dy in d: 를 사용할 경우 시간 초과가 뜸
            # for range와 for in list의 메모리 차이는 매우크게난다.
            # 왜 메모리차이가 크게 날까? => 메모리를 많이 할당할 수록 cpu가 할일이 많다는 뜻 그러므로 시간 초과 발생.
            # range객체에서는 모든 값을 계산해서 미리 기억하고 있는 것이 아니라
            # 요구할 때 마다 매개변수로 받은 값들을 기반으로
            # 연산하여 그때마다 결과를 돌려주기 때문이다.
            # 참고 문서 https://docs.python.org/3/library/stdtypes.html#range
            # 참고 블로그 https://haruhiism.tistory.com/137

res = 0
r, c = map(int, input().split())
alpha_lst = [list(input()) for _ in range(r)]
lst = set()    # set에서 in을 쓰면 해시로 찾기 때문에 O(1), list에서는 O(n)
lst.add(alpha_lst[0][0])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dfs(0, 0, 1)

print(res)
