class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums = sorted(nums, key=lambda x: 1 if x > pivot else (0 if x == pivot else -1))
        return nums