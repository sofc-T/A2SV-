class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        double = {"IV",
            "IX",
            "XL",
            "XC",
            "CD",
            "CM"}
        ans, l= 0, 0
        while l < len(s):
            if l < len(s) - 1:
                if s[l:l+2] in double:
                    ans += roman[s[l:l+2]]
                    l += 2
                else:
                    ans += roman[s[l]]
                    l += 1
            else:
                ans += roman[s[l]]
                l += 1
            # print(ans)
        return ans
