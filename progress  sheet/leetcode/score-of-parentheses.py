class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for chr in s:
            print(stack)
            if chr  == "(":
                stack.append(0)
            else:
                last_element = stack.pop()
                stack[-1] += max(1,last_element * 2)
        return stack[0]