class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l, r = 0, 0
        while l < len(name) and r < len(typed):
            if name[l] == typed[r]:
                l += 1
                r += 1
            elif r > 0 and typed[r-1] == typed[r]:
                r += 1
            else:
                # print(l)
                return False
        if l < len(name):
            return False
        while r < len(typed):
            if typed[r-1] == typed[r]:
                r += 1
            else:
                return False
        return True