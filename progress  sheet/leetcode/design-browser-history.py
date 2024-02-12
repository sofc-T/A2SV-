class ListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.curN = self.head

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.curN.next = newNode
        newNode.prev = self.curN
        self.curN = self.curN.next

    def back(self, steps: int) -> str:
        while self.curN and self.curN.prev and steps:
            self.curN = self.curN.prev
            steps -= 1
        return self.curN.val

    def forward(self, steps: int) -> str:
        while self.curN and self.curN.next and steps:
            self.curN = self.curN.next
            steps -= 1
        return self.curN.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)