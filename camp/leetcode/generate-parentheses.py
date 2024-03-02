class Solution(object):
    def generateParenthesis(self, n):
        
        def Generate_Parentheses(sentence, left, right):
            if len(sentence) == n * 2:
                l.append(sentence)
                return
            if left < n:
                Generate_Parentheses(sentence + '(', left + 1, right)
            if right < left:
                Generate_Parentheses(sentence + ')', left, right + 1)

        l = []
        Generate_Parentheses('',0,0)
        return l