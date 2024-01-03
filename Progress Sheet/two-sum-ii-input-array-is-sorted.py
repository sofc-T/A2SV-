class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            val = nums[l] + nums[r]
            if val == target:
                return [l+1,r+1]
            elif val < target:
                l += 1
            else:
                r -= 1