class Solution:
    def decodeString(self, sin: str) -> str:
        stack = []
        s = ""
        num = 0
        
        for chr in sin:
            if chr.isdigit():
                num = (num * 10) + int(chr)
            elif chr == "[":
                stack.append(num)
                stack.append(s)
                s, num = "", 0
            elif chr == "]":
                ps = stack.pop()
                pnum = stack.pop()
                s = ps + (pnum * s)
            else:
                s += chr
        return  s + "".join(stack)[::-1] 