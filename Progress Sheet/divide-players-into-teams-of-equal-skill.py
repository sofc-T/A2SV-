class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        l,r =0, len(skill) - 1
        skillCurr = skill[l] + skill[r]
        while l < r:
            skillCur = skill[l] + skill[r]
            if skillCur != skillCurr:
                return -1
            chemistry += skill[l] * skill[r]
            l += 1
            r -= 1
        return chemistry