# URL: https://leetcode.com/problems/valid-parentheses/

def isValid(s):
    stack = []
    closeToOpen = {")":"(", "}":"{", "]":"["}

    for c in s:
        # If its a closing bracket
        if c in closeToOpen:
            # Make sure the stack is not empty
            # And the value at the top of the stack is a matching opening bracket
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
            
        # If its a opening bracket
        else:
            stack.append(c)

    # Return true if stack is empty
    if not stack: return True
    else: return False
    

if __name__ =="__main__":
    s = "()[]{}"
    print(isValid(s))