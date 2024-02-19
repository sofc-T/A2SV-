class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == "+":
                second_elem = stack.pop()
                stack[-1] = int(stack[-1]) + int(second_elem)
            elif val == "-":
                second_elem = stack.pop()
                stack[-1] = int(stack[-1]) - int(second_elem)
            elif val == "*":
                second_elem = stack.pop()
                stack[-1] = int(stack[-1]) * int(second_elem)
            elif val == "/":
                second_elem = stack.pop()
                stack[-1] = int(stack[-1]) / int(second_elem)
            else:
                stack.append(val)
        return int(stack[0])