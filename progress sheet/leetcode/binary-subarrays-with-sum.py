class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        psum = {}
        ans, total = 0 , 0
        for num in nums:
            total += num
            if total - goal == 0:
                ans += 1
            if total - goal in psum:
                ans += psum[total-goal]
            if total in psum:
                psum[total] += 1
            else:
                psum[total] = 1
        return ans