class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, ans = [], [-1 for _ in range(len(nums))]
        for idx,val in enumerate(nums):
            while stack and val > nums[stack[-1]]:
                ans[stack[-1] ] = val
                stack.pop()
            stack.append(idx)
        for idx,val in enumerate(nums):
            while stack and val > nums[stack[-1]]:
                ans[stack[-1] ] = val
                stack.pop()
            stack.append(idx)
        return ans