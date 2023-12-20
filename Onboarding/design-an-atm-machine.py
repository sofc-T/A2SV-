class ATM:

    def __init__(self):
        self.acc = [0] * 5
        self.total = 0
        self.vals =[20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for idx in range(len(banknotesCount)):
            self.acc[idx] += banknotesCount[idx]
            self.total += banknotesCount[idx] * self.vals[idx]

    def withdraw(self, amount: int) -> List[int]:
        if self.total < amount:
            return [-1]
        elif self.total == amount:
            temp = self.acc[:]
            self.acc = [0] * 5
            return temp
        res = [0] * 5
        temp = self.acc[:]
        curr_amnt = amount
        for idx in range(4,-1,-1):
            curr_notes = curr_amnt // self.vals[idx]
            if curr_notes > temp[idx]:
                curr_notes = temp[idx]
            if curr_notes:
                res[idx] = curr_notes
                temp[idx] -= curr_notes
                curr_amnt -= curr_notes * self.vals[idx]
        if curr_amnt == 0:
            self.total -= amount
            self.acc = temp[:]
            return res
        else:
            return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)