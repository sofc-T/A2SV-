class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, three = [], inf * -1
        for idx in range(len(nums)-1,-1,-1):
            if nums[idx] <  three:
                return True
            while stack and stack[-1] < nums[idx]:
                three = stack.pop()
            stack.append(nums[idx])
        return False
