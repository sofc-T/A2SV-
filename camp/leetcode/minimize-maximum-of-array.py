class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxx, running = -1, 0
        for idx,num in enumerate(nums):
            running += num
            maxx = max(maxx,ceil(running/(idx+1)))
        return maxx
        