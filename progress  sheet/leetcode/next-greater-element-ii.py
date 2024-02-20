class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, ans = [], [-1 for _ in range(len(nums))]
        for idx in list(range(len(nums)))*2:
            while stack and nums[idx] > nums[stack[-1]]:
                ans[stack[-1] ] = nums[idx]
                stack.pop()
            stack.append(idx)
        return ans