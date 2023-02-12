par_str = list(input())
str_stack = []  # making a str_stack to check and pop from the str
i = 0 
result = 0
tmp = 1

for i in range(len(par_str)):
    if par_str[i] == "(":  #  if str is '(' than add it to the stack
        str_stack.append(par_str[i])
        tmp *= 2
        
    elif par_str[i] == "[":
        str_stack.append(par_str[i])
        tmp *= 3
       
    elif par_str[i] == ")":  # if face with ')' pop the top idx of the stack
        if not str_stack and str_stack[-1] == "[":  # Check if stack is not empty and last element is "["
            break
        if par_str[i-1] == "(":
            result += tmp
        str_stack.pop()
        tmp //= 2
                
    elif par_str[i] == "]":
        if not str_stack and str_stack[-1] == "(":  # Check if stack is not empty and last element is "("
            break
        if par_str[i-1] == "[":
            result += tmp
        str_stack.pop()
        tmp //= 3
        
if str_stack:
    print(0)
else:
    print(result)