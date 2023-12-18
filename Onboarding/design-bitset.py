class Bitset:

    def __init__(self, size: int):
        self.bitset = ["0"] * size
        self.bitsetfpd = ["1"] * size
        self.c = 0
        self.size = size
    def fix(self, idx: int) -> None:
        if self.bitset[idx] ==  "0":
            self.bitset[idx] = "1"
            self.bitsetfpd[idx] = "0"
            self.c += 1
    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == "1":
            self.bitset[idx] = "0"
            self.bitsetfpd[idx] = "1"
            self.c -= 1

    def flip(self) -> None:
        self.bitsetfpd, self.bitset = self.bitset, self.bitsetfpd
        self.c = self.size - self.c
    def all(self) -> bool:
       return self.c == self.size

    def one(self) -> bool:
        return self.c > 0

    def count(self) -> int:
        return self.c

    def toString(self) -> str:
        return "".join(self.bitset)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.c()
# param_7 = obj.toString()