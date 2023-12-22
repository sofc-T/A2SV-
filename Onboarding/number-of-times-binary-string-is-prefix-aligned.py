class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        total, count = 0, 0
        maxx = 0
        for num in flips:
            total += num
            maxx = max(maxx,num)
            if (maxx * (maxx + 1)) / 2 == total:
                count += 1
        return count 