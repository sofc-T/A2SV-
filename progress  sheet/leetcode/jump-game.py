class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for r in range(len(nums)-2,-1,-1):
            if nums[r] >= last - r :
                last = r
        return last == 0