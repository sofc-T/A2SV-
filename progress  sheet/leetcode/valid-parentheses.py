class Solution:
    def isValid(self, s: str) -> bool:
        closing = {"]","}",")"}
        valids = {"{":"}", "[":"]","(":")"}
        stack = []
        for chr in s:
            if chr in closing:
                if stack and valids[stack[-1]] == chr:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(chr)
        return len(stack) == 0