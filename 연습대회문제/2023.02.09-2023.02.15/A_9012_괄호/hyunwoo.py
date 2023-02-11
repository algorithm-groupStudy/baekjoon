# import sys
# sys.stdin = open('input.txt')

# t= int(input())  # input number of test_case

# for test_case in range(1,t+1): 
#     par_str= input().split()
#     str_stack = []  # making a str_stack to check and pop from the str
    
#     i = 0 
#     while len(par_str[0]) > i:
#         print(par_str[0][i])
#         print(str_stack)
#         if len(par_str) == i:
#             if str_stack:
#                 print(f'{test_case} NO')
#             else:
#                 print(f'{test_case} YES')
#         elif par_str[0][i] == "(":  #  if str is '(' than add it on the stack
#             str_stack.append(par_str[0][i])
#         elif par_str[0][i] == ")":  # if face with ')' pop the top idx of the stack
#             if str_stack:
#                 tmp = str_stack.pop() # to do this we need to check whether there is index in the stack
#                 if tmp != "(":
#                     print(f"{test_case} NO")
#                     i = len(par_str[0])+1
#             else:
#                 print(f"{test_case} NO")
#                 i = len(par_str[0])+1
#         i += 1
    

import sys
sys.stdin = open('input.txt')

www



        