class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        vals = zip(*strs)
        count = 0
        for col in vals:
            if list(col) != sorted(col):
                count += 1
        return count