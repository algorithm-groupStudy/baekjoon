paren = input()
stack = []

def check_paren():
    pairs = {')': '(', ']': '['}
    if len(paren) == 2:
        score = 0
        if p == '(' or p == 




for p in paren:
    if p == '(' or p =='[':
        stack.append(p)


([()([])])



''' 
2: ( temp = 2 
3: [ temp = 2, 3 
2: ( temp = 2, 3, 2 

pop 2 


