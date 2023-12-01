class Solution:
    def average(self, salary: List[int]) -> float:
        minn, maxx = inf, -1 * inf
        total = 0
        for money in salary:
            if money < minn:
                minn = money
            if money > maxx:
                maxx = money
            total += money
        return (total - minn - maxx) / (len(salary) - 2)