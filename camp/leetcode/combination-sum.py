class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def findCands(total,level,idx):
            if total == target:
                ans.append(level[:])
                return
            for j in range(idx,len(candidates)):
                if total + candidates[j] > target:
                    continue
                level.append(candidates[j])
                total += candidates[j]
                findCands(total,level,j)
                total -= candidates[j]
                level.pop()
            return ans
        return findCands(0,[],0)