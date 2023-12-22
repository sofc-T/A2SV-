class Solution:
    def validMountainArray(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        l = 1
        while l < len(nums) and nums[l] > nums[l-1]:
            l += 1
        if l == len(nums) or  l == 1: return False
        while l < len(nums) and nums[l] < nums[l-1]:
            l += 1
        return  l == len(nums)