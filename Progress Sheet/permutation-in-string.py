class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ss1 =set(s1)
        cs1 = Counter(s1)
        for r in range(len(s2)):
            if s2[r] in ss1:
                if Counter(s2[r:r+len(s1)]) == cs1:
                    return True
        return False