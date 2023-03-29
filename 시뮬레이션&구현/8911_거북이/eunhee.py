import sys
sys.stdin=open("test.txt")
# 다시풀기 
dx=[0,1,0,-1]
dy=[1,0,-1,0]

t = int(input())
for tc in range(t):
    arrow = list(input())
    
    direction=0
    x,y=0,0
    route = [(x,y)]
    for d in arrow:
        if d=="F":
            x+=dx[direction]
            y+=dy[direction]
        elif d=="B":
            x-=dx[direction]
            y-=dy[direction]
        elif d=="L":
            if direction==0:
                direction=3
            else:
                direction-=1
           
        elif d=="R":
            if direction==3:
                direction=0
            else:
                direction+=1
           
            
        route.append((x,y))
    width = max(route,key=lambda x:x[0])[0] - min(route, key=lambda x:x[0])[0]
    height = max(route,key=lambda x:x[1])[1] - min(route, key=lambda x:x[1])[1]
    print(width*height)
