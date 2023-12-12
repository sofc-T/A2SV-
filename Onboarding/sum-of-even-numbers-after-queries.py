class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        total_evens = sum([x for x in nums if x % 2 == 0])
        for val, ind in queries:
            temp = nums[ind]
            nums[ind] += val
            if temp % 2 == 0:
                total_evens -= temp
            if nums[ind] % 2 == 0:
                total_evens += nums[ind]
            res.append(total_evens)
        return res