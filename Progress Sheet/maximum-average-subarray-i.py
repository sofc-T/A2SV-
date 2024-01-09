class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l , r = 0 , k 
        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == k:
            return sum(nums)/k
        summ = sum(nums[:k])

        max_sum = summ
        while r < length:
            
            summ = summ - nums[l] + nums[r]
            max_sum = max(summ,max_sum)
            r += 1
            l += 1

        return max_sum/k