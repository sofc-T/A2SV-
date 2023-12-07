class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        res = []
        for word in words:
            if word[0].lower() in row1:
                valo = 1
            elif word[0].lower() in row2:
                valo = 2
            else:
                valo = 3
            for letter in word:
                if letter.lower() in row1:
                    val = 1
                elif letter.lower() in row2:
                    val = 2
                else:
                    val = 3
                if valo != val:
                    break
            if val == valo:
                res.append(word)
        return res
                
