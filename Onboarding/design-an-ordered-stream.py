class OrderedStream:

    def __init__(self, n: int):
        self.length = n
        self.store = [0] * n
        self.start = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.store[idKey-1] = value
        c = self.start
        while c < len(self.store) and self.store[c]:
            c += 1
        temp = self.start
        self.start = c
        return self.store[temp:c]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)