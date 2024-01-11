class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len, total = inf, 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            while total > target:
                if total - nums[l] < target:
                    break
                total -= nums[l]
                l += 1
            if total >= target:
                min_len = min(min_len,r-l+1)
            # print(min_len,l,r)
        if l == 0 and total < target:
            return 0
        return min_len 