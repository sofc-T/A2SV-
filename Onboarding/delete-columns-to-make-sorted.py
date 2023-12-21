class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        vals = list(strs[0])
        count, unsorted = 0, set()
        for idx in range(1,len(strs)):

            for j in range(len(strs[idx])):
                if strs[idx][j] < vals[j]:
                    if j not in unsorted:
                        count += 1
                        unsorted.add(j)
                vals[j] = strs[idx][j]
        return count