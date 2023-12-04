class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i, res = 0, []
        while i < len(nums)-1:
            res += [nums[i+1]] * nums[i]
            i += 2
        return res