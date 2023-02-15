s = input()
stack=[]
min_val =''
max_val =''
for i in s:
    if i=='M':
        if i not in stack:
            min_val+='1'
        else:
            min_val+='0'
        stack.append(i)
    else:
        max_val+='5'+'0'*len(stack)
        min_val+='5'
        stack = []
max_val+= '1'*len(stack)    
print(max_val)
print(min_val)