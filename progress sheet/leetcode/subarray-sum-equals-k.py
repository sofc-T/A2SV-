class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psum = {}
        total = 0 
        ans = 0
        for num in nums:
            total += num
            if total - k == 0:
                ans += 1 
            if total - k in psum:
                ans += psum[total-k]
            if total in psum:
                psum[total] += 1
            else:
                psum[total] = 1 
        return ans