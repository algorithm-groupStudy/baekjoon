import math 

X, Y = map(int, input().split())


def ans(X, Y):

    Z = (Y * 100) // X 
    if Z == 100 or Z == 99: 
        return -1
    target = (100 * Y - X * (Z + 1)) / (Z + 1 - 100)
    return math.ceil(target)     

print(ans(X, Y))