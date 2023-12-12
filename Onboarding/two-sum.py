class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0 , len(nums) - 1
        store = {}
        for ind, val in enumerate(nums):
            if target - val in store:
                return [store[target-val],ind]
            store[val] = ind
