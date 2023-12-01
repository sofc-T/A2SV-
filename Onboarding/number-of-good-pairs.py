class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c, store = 0, {}
        for i in range(len(nums)):
            val = store.get(nums[i],-1)
            if val != -1:
                c += val
                store[nums[i]] += 1
            else:
                store[nums[i]] = 1
        return c