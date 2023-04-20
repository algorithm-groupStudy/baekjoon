# N = int(input())
# pos = input()
# board = [[0 for _ in range(N)] for _ in range(N)]
# x,y = ord(pos[0])-97,int(pos[1])-1
# cnt=0
# dx = [-2,-2,-1,-1,1,1,2,2]
# dy = [-1,1,-2,2,-2,2,-1,1]
# for i in range(8):
#     nx,ny = x+dx[i],y+dy[i]
#     if 0<=nx<N and 0<=ny<N:
#         cnt+=1
# print(cnt)
lst = list(input())
lst.sort()
total=0
res = ""
for i in range(len(lst)):
    if lst[i].isdigit():
        total+=int(lst[i])
    else:
        res+="".join(lst[i:])+str(total)
        break
print(res)
