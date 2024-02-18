class RecentCounter:

    def __init__(self):
        self.store = deque()

    def ping(self, t: int) -> int:
        self.store.appendleft(t)
        while t - self.store[-1] > 3000:
            self.store.pop()
        return len(self.store)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)