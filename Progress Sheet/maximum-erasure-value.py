class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seenAt = {}
        l, r = 0 , 0
        maxSum, currSum = 0, 0
        while r < len(nums):
            if nums[r] in seenAt  and seenAt[nums[r]] >= l:
                maxSum = max(maxSum,currSum)
                while l < seenAt[nums[r]]:
                    currSum -= nums[l]
                    l += 1
                l += 1
                seenAt[nums[r]] = r
                r += 1
            else:
                currSum += nums[r]
                seenAt[nums[r]] = r
                r += 1
        return max(maxSum,currSum)