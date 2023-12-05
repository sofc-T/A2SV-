class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        r = len(nums) - 1
        while r > 1:
            if nums[r-1] + nums[r-2] > nums[r]:
                return nums[r-1] + nums[r-2] + nums[r]
            else:
                r -= 1
        return 0