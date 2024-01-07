class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l, r= 0, 0
        true, false = 0, 0
        while r < len(answerKey):
            # print(l,r,true,false)
            if answerKey[r] == "T":
                true += 1
            else:
                false += 1
            if min(true,false) >= k + 1:
                if answerKey[l] == "T":
                    true -= 1
                else:
                    false -= 1
                l += 1
            r += 1
        # print(r,l)
        return r - l