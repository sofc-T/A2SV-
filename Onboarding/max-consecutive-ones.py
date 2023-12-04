class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c, max_c = 0, 0
        for num in nums:
            if num == 1:
                c += 1
            else:
                max_c = max(c,max_c)
                c = 0
        return max(max_c,c)