class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left ,right= 0,1
        
        while right < n:
            if nums[left] == 0 and nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
            elif nums[left] == 0 and nums[right] ==0:
                right += 1
                continue
            right += 1
            left += 1
        
        
        