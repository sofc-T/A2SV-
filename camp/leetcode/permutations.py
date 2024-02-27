class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def permute(level):
            if len(level) == len(nums):
                ans.append(level[:])
                return 
            
            for idx in range(len(nums)):
                if nums[idx] not in level:
                    level.append(nums[idx])
                    permute(level)
                    level.pop()
            return ans
        return permute([])