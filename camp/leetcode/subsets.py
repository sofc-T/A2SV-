class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def powerSet(level,idx):
            ans.append(level[:])
            if idx == len(nums):
                
                return 
            for j in range(idx,len(nums)):
                level.append(nums[j])
                powerSet(level,j+1)
                level.pop()
            return ans
        return powerSet([],0)