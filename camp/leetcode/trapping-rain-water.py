class Solution:
    def trap(self, height: List[int]) -> int:
        stack, water = [], 0
        for idx,block in enumerate(height):
            while stack and block >= stack[-1][0]:
                water += (min(block,stack[0][0]) - stack[-1][0]) * (idx - stack[-1][1] )
                idx = stack.pop()[1]
            stack.append((block,idx))
        return water
