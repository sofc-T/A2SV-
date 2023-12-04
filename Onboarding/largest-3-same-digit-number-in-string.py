class Solution:
    def largestGoodInteger(self, num: str) -> str:
        val = num[0]
        res = []
        c = 1
        for chr in num[1:]:
            if chr == val:
                c += 1
                if c == 3:
                    res.append(int(val*3))
            else:
                val = chr
                c = 1
        if not res: return ""
        if max(res) == 0:return "000"
        return str(max(res))