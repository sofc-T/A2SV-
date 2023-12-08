class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n//7
        days = n % 7
        bank = 0
        for week in range(full_weeks):
            bank += sum(range(week +1 ,week + 8 ))
        bank += sum(range(full_weeks + 1 , full_weeks + days + 1))
        return bank