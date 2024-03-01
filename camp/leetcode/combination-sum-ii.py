class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def backtrack(number_idx,comb,total):
            if total == target:
                ans.append(comb[:])
                return
            if number_idx >= len(candidates):
                return 
            for idx in range(number_idx,len(candidates)):
                if total + candidates[idx] > target:
                    break
                if idx > number_idx and candidates[idx] == candidates[idx - 1]:
                    continue
                total += candidates[idx]
                comb.append(candidates[idx])
                backtrack(idx + 1,comb,total)
                total -= comb.pop()
            return ans
        return backtrack(0,[],0)