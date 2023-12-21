class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        minn = nums[0]
        if nums[1] > minn:
            i = 2
            point = nums[1]
        else:
            point = inf
            i = 1
        for j in range(i,len(nums)):
            if nums[j] > point:
                return True
            if nums[j] < minn:
                minn = nums[j]
            elif nums[j] < point and nums[j] > minn:
                point = nums[j]
        return False