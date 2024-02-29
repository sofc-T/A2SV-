class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        seenAt = {0:-1}
        running, total = 0, sum(nums)
        min_len = inf
        
        if total % p == 0:
            return 0
        for idx, num in enumerate(nums):
            running += num
            if num == total % p:
                return 1
            if (running - total) % p in seenAt:
                min_len = min(min_len, idx - seenAt[(running - total) % p])
            seenAt[running % p] = idx
            
        return min_len if min_len < len(nums) else -1
