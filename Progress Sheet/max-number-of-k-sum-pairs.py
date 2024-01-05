class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r= 0, len(nums) - 1
        operations = 0
        while l < r:
            total = nums[l] + nums[r]
            if total == k:
                operations += 1
                l += 1
                r -= 1
            elif total < k:
                l += 1
            else:
                r -= 1
        return operations