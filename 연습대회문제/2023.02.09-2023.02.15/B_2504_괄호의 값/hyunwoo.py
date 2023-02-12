par_str = input().split()
str_stack = []  # making a str_stack to check and pop from the str
    
i = 0 
result = 0
tmp = 1
while i < len(par_str[0]):
    print(f'{i} i')
    if par_str[0][i] == "(":  #  if str is '(' than add it on the stack
        str_stack.append(par_str[0][i])
        tmp *= 2
        
    elif par_str[0][i] == "[":
        str_stack.append(par_str[0][i])
        tmp *= 3
            
    elif par_str[0][i] == ")":  # if face with ')' pop the top idx of the stack
        if str_stack and str_stack[-1] == "(":  # Check if stack is not empty and last element is "("
            print(tmp)
            result += tmp
        else:
            result = 0
            break
        str_stack.pop()
        tmp //= 2
                
    elif par_str[0][i] == "]":
        if str_stack and str_stack[-1] == "[":  # Check if stack is not empty and last element is "["
            result += tmp
            print(tmp)
        else:
            result = 0
            break
        str_stack.pop()
        tmp //= 3
    print(f'{result} result')
    i += 1
        
if str_stack:
    result = 0
else:
    print(result)
