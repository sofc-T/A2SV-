class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        def findCands(total,level):
            if total == target:
                ans.add(tuple(sorted(level)))
                return
            for j in range(len(candidates)):
                # print(level,ans)
                if total + candidates[j] > target:
                    continue
                level.append(candidates[j])
                total += candidates[j]
                findCands(total,level)
                total -= candidates[j]
                level.pop()
            return ans
        candidates.sort()
        return findCands(0,[])