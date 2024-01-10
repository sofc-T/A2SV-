class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # result = []
        minn = float('inf')

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                diff = abs(s - target)
                if diff < minn:
                    minn = diff
                    ans = s
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    ans = s
                    j += 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1

        return ans