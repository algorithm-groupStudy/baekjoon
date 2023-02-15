T = int(input())
for tc in range(1,T+1):
    s = map(str,input())
    stack =[]
    top =-1
    answer ='NO'
    for i in s:
        if top==-1:
            if i ==')':
                break
            else:
                stack.append(i)
                top +=1
        else:
            if i==')':
                if stack[top]=='(':
                    stack.pop()
                    top -=1
                else:
                    break
            else:
                stack.append(i)
                top+=1
    else:
        if stack==[]:
            answer ='YES'
    print(answer)