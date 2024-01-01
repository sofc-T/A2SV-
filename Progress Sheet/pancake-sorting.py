class Solution:
    def pancakeSort(self, nums: List[int]) -> List[int]:
        indcs = []
        def flip(nums,k):
            nums[:k] = nums[:k][::-1]
        correct = sorted(nums)
        j = len(nums) - 1
        # j = 0
        # while j < len(nums):
        while j > -1:
            i = 0
            while nums[i] != correct[j]:
                i += 1
            flip(nums,i+1)
            flip(nums,j+1)
            indcs.append(i+1)
            indcs.append(j+1)
            j -= 1
        return indcs