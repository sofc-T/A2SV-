class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def powerSet(level,idx):
            ans.add(tuple(sorted(level)))
            if idx == len(nums):
                
                return 
            for j in range(idx,len(nums)):
                level.append(nums[j])
                powerSet(level,j+1)
                level.pop()
            return ans
        return powerSet([],0)