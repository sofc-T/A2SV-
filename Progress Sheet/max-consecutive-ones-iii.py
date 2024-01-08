class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        while r < len(nums):
            if not nums[r]:
                k -= 1
            r += 1
            if k < 0:
                if not nums[l]:
                    k += 1
                l += 1
        return r - l 