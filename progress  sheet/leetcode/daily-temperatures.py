class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, ans = [], [0 for _ in range(len(temperatures))]
        for idx,val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                # print(stack)
                ans[stack[-1]] = idx - stack[-1]
                stack.pop()
            stack.append(idx)
        return ans