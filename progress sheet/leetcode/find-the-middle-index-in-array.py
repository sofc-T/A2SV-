class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        lefts, rights = 0, sum(nums)
        for i in range(len(nums)):
            if lefts == rights - nums[i]: return i
            lefts += nums[i]
            rights -= nums[i]
        return -1