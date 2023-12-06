class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        l, r = 0, n 
        for ind in range(n):
            res.append(nums[ind])
            res.append(nums[ind + n])
        return res