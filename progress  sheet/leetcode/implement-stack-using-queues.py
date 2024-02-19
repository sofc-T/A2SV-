class MyStack:

    def __init__(self):
        self.ds = []

    def push(self, x: int) -> None:
        self.ds.append(x)        

    def pop(self) -> int:
        return self.ds.pop()

    def top(self) -> int:
        return self.ds[-1]

    def empty(self) -> bool:
        return len(self.ds) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()