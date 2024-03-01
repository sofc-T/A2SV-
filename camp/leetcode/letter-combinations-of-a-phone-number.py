class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        ans = []
        def backtrack(digit_index,letter_index,curr_string):
            if len(curr_string) == len(digits):
                ans.append("".join(curr_string))
                return
            for letter_index in range(len(mapping[digits[digit_index]])):
                curr_string.append(mapping[digits[digit_index]][letter_index])
                
                backtrack(digit_index+1,letter_index,curr_string)
                curr_string.pop()
            return ans
        return backtrack(0,0,[])
        
