class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        if len(nums) < 3:
            return True
        if nums[0] > nums[1]:
            if nums[0] > nums[2]:
                nums[0] = nums[1]
                count += 1
            else:
                nums[1] = nums[0]
                count += 1
        for ind in range(2,len(nums)):
            if nums[ind] < nums[ind-1]:
                if nums[ind-2] > nums[ind]:
                    nums[ind] = nums[ind-1]
                    count += 1
                else:
                    count += 1
                    nums[ind-1] = nums[ind] - 1
        return count < 2
        