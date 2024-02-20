class MinStack:

    def __init__(self):
        self.stack = []
        self.minn= inf
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minn = min(self.minn,val)
    def pop(self) -> None:
        if self.stack[-1] == self.minn:
            self.stack.pop()
            if self.stack:   
                self.minn = min(self.stack)
            else:
                self.minn = inf
        else:
            self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()