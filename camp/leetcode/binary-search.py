class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = (len(nums) - 1) // 2
        l, r = 0, len(nums) - 1
        temp = inf
        while nums[mid] != target:
            if l >= r:
                return -1
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
            mid = (r + l) // 2
        return mid 