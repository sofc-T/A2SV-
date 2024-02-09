class Solution:
    def minimumSteps(self, s: str) -> int:
        # l, r = 0 , 0
        # while l < len(s) and s[l] == "0":
        #     l += 1
        #     r += 1
        # count = 0
        # while l < len(s) and r  < len(s):
        #     if s[r] == "0":
        #         count += r - l
        #         l += 1
        #         r += 1
        #     else:
        #         r += 1
        # return count

        black, moves = 0 , 0
        for val in s:
            if val == "1":
                black += 1
            else:
                moves += black
        return moves