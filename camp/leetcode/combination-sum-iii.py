class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(num,comb,total):
            if total == n and len(comb) == k:
                ans.append(comb[:])
                return
            for curr in range(num,10):
                if len(comb) == k or total >= n:
                    break
                total += curr
                comb.append(curr)
                backtrack(curr+1,comb,total)
                total -= comb.pop()
            return ans
        return backtrack(1,[],0)
            