class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        psum = {}
        ans = total = 0
        for num in nums:
            total += num
            if total % k == 0:
                ans += 1
            if total % k in psum:
                ans += psum[total % k]
            if total % k in psum:
                psum[total % k] += 1
            else:
                psum[total % k] = 1
        return ans