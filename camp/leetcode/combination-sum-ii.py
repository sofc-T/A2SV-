class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def backtrack(idx,comb,total):
            if total == target:
                ans.append(comb[:])
                return
            if idx >= len(candidates):
                return 
            for i in range(idx,len(candidates)):
                if total + candidates[i] > target:
                    break
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                total += candidates[i]
                comb.append(candidates[i])
                backtrack(i + 1,comb,total)
                total -= comb.pop()
            return ans
        return backtrack(0,[],0)