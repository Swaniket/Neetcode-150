# URL: https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Adding value to Min Stack
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]


if __name__ =="__main__":
    obj = MinStack()

    vals = [-2,0,-3]
    for val in vals:
        obj.push(val)

    print("1st Min", obj.getMin())
    obj.pop()
    print("Top", obj.top())
    print("2nd Min", obj.getMin())