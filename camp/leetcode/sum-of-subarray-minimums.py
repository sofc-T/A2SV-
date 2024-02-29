class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack =  [-1]
        ans = 0
        for idx,val in enumerate(arr):
            while stack[-1] != -1  and val < arr[stack[-1]]:
                ans += arr[stack[-1]] * ((stack[-1] - stack[-2]) * (idx - stack[-1]))
                stack.pop()
            stack.append(idx)
        # print(stack)
        for idx in range(len(stack) -1, 0 , -1):
            # print((len(arr)  - stack[idx]) , (stack[idx] - stack[idx-1]) , arr[stack[idx]])
            ans += (len(arr)  - stack[idx]) *  (stack[idx] - stack[idx-1]) * arr[stack[idx]]
        return ans % (10**9 + 7)