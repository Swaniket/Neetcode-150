# URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/

def EvalPolish(tokens):
    stack = []

    for token in tokens:
        if token == "+":
            # Add the last 2 popped element
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            # We need to substract the 2nd element from the first element
            a, b = stack.pop(), stack.pop()
            stack.append(b-a)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            a, b = stack.pop(), stack.pop()
            # Typecast to int to trancade toward 0
            stack.append(int(b/a))
        else:
            stack.append(int(token))

    # Because its gareteed to have one element in the stack
    return stack[0]


if __name__ =="__main__":
    tokens1 = ["2","1","+","3","*"] # OP - 9
    tokens2 = ["4","13","5","/","+"] # OP - 6
    tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # OP - 22

    print(EvalPolish(tokens1))