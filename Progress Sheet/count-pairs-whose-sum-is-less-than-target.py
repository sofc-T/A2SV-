class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        c = 0
        l, r = 0, len(nums) - 1
        while l < r:
            while r > l and nums[l] + nums[r] >= target:
                r -= 1
            if r <= l:                
                break
            c += r - l
            l += 1
        return c