class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total, maxx = 0 , -1 * inf
        for num in nums:
            total += num
            maxx = max(maxx,total)
            if total < 0:
                total = 0
            
        return maxx