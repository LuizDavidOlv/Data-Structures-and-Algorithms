listSize = 3
s = "{[(])}"
s1 = "([]())[]{[([[]])()]}"  
s2 = "){"
inputList = [listSize, s, s1, s2]

def isValid(s):
    stack = [] # create an empty stack to store opening brackets
    for c in s: # loop through each character in the string
        if c in '([{': # if the character is an opening bracket
            stack.append(c) # push it onto the stack
        else: # if the character is a closing bracket
            if not stack or (c == ')' and stack[-1] != '(') or (c == '}' and stack[-1] != '{') or (c == ']' and stack[-1] != '['):
                return False # the string is not valid, so return false
            stack.pop() # otherwise, pop the opening bracket from the stack
    return not stack # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
                        # so the string is valid, otherwise, there are unmatched opening brackets, so return false



def isValidList(inputList):
    result = []
    listSize = inputList[0]
    for listIndex in range(1, listSize+1):
        add = True
        stack = [] 
        s = inputList[listIndex]
        for c in s: 
            if c in '([{': 
                stack.append(c) 
            else: 
                if not stack or \
                (c == ')' and stack[-1] != '(') or \
                (c == '}' and stack[-1] != '{') or \
                (c == ']' and stack[-1] != '['):
                    result.append("NO")
                    add = False
                    break
                stack.pop() 
        if not stack and add:
            result.append("YES")
    return result
    
print(isValidList(inputList)) 