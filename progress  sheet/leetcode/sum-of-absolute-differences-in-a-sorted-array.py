class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        psum = 0
        for ind, val in enumerate(nums):    
            nums[ind] = abs(psum - (val * (ind))) + abs(total - psum - (val * (len(nums)-ind)))
            psum += val
        return nums