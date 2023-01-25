num_egg = int(input())
egg_list = []
for num in range(num_egg):
    a, b = input().split()
    egg_list.append({'durability': a, 'weight' : b})

def egg_break(list):
    list[0] 
# list의 가장 왼쪽 계란을 든다. 
# 바로 오른쪽 계란을 친다. 
# 들고있던 계란이 깨졌다면, 깨진 계란의 갯수를 구해라
# 들고있던 계란이 깨지지 않았다면, 그 다음 계란을 친다. 

# 오른쪽 두번째 계란을 친다. 
# 들고있던 계란이 깨졌다면, 깨진 계란의 갯수를 구해라.
# 들고 있던 계란이 깨지지 않았다면, 그 다음 계란을 친다. 

# 이렇게 하는게 아니고, durability값이 낮고, weight 값도 가장 낮은 계란을 찾아서 치는건가? 
# 그 순서대로 푸는건가..? 내일 풀어봐야징 
