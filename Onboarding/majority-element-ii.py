class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        store = {}
        res, limit = [], len(nums)//3
        for num in nums:
            store[num] = store.get(num,0) + 1
            if store[num] == limit + 1:
                res.append(num)
        return res