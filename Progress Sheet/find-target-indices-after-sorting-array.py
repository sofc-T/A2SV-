class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        for idx in range(len(nums)):
            if nums[idx] == target:
                res.append(idx)
        return res
            