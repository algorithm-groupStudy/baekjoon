import sys
sys.stdin = open('input.txt')

def reward_a(rank):
    if rank == 0:
        return 0 
    
    if rank == 1:
        return 500
    elif rank <= 3:
        return 300
    elif rank <= 6:
        return 200
    elif rank <= 10:
        return 50
    elif rank <= 15:
        return 30
    elif rank <= 21:
        return 10
    else:
        return 0
    
def reward_b(rank):
    if rank == 0:
        return 0

    if rank == 1:
        return 512
    elif rank <= 3:
        return 256
    elif rank <= 7:
        return 128
    elif rank <= 15:
        return 64
    elif rank <= 31:
        return 32
    else :
        return 0
    
t = int(input())
for case in range(1,1+t):
    a, b = map(int, input().split())
    result = reward_a(a) + reward_b(b)
    print(result*10000)

