

# def check(num):
#     for s in num:
#         if "3" in str(s):
#             return 1
#     return 0

# time=[0,0,0]
# cnt=0
# while True:
#     if time[0]==N and time[1]==59 and time[2]==59:
#         break
#     time[2]+=1
#     if time[2]==60:
#         time[2]=0
#         time[1]+=1
#     if time[1]==60:
#         time[1]=0
#         time[0]+=1
    
#     cnt+=check(time)
# print(cnt)
N,K = map(int,input().split())
cnt=0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if str(K) in str(i).zfill(2)+str(j).zfill(2)+str(k).zfill(2):
                cnt+=1
print(cnt)