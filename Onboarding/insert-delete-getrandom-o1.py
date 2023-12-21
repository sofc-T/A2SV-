class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        present = val in self.map
        if not present:
            self.map[val] = len(self.vals)
            self.vals.append(val)
        return not present

    def remove(self, val: int) -> bool:
        res = val in self.map
        if res:
            temp = self.map[val]
            tempval = self.vals[-1]
            self.vals[temp], self.vals[-1] = self.vals[-1], self.vals[temp]
            self.map[tempval] = temp
            self.vals.pop()
            self.map.pop(val)
        return res

    def getRandom(self) -> int:
        randNum = random.randint(0,len(self.vals)-1)
        val = self.vals[randNum]
        return val


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()