class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds, goods = 0, 0
        count = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                odds += 1
                count = 0
            if odds == k:
                while nums[l] % 2 == 0:
                    count += 1
                    l += 1
                count  += 1 
                l += 1
                odds -= 1
            goods += count
        return goods