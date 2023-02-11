t = int(input())  # input number of test_case

for test_case in range(1, t + 1): 
    par_str = input().split()
    str_stack = []  # making a str_stack to check and pop from the str
    
    i = 0 
    result = 0
    while i < len(par_str[0]):
        if par_str[0][i] == "(":  #  if str is '(' than add it on the stack
            str_stack.append(par_str[0][i])
        elif par_str[0][i] == ")":  # if face with ')' pop the top idx of the stack
            if str_stack:
                tmp = str_stack.pop() # to do this we need to check whether there is index in the stack
                if tmp != "(":
                    result += 3
            else:
                result = "NO"
                break
        i += 1
        
    if str_stack:
        result = "NO"
        
    print(f"{result}")