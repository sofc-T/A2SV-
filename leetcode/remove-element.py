class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums.sort(key= lambda x : 1 if x == val else 0)
        # while nums and nums[-1] == val:
        #     nums.pop()

        l, r = 0 , 0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l