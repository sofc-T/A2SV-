class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        store = {num:ind for ind, num in enumerate(nums)}
        for x, y in operations:
            nums[store[x]] = y
            store[y] = store[x]
        return nums