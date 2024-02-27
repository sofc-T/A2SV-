class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(level,n,k,res):
            if len(level) == k:
                res.append(level[:])
                return 
            s = level[-1] if level  else 0
            for candidate in range(s,n):
                level.append(candidate + 1)
                backtrack(level,n,k,res)
                level.pop()
            return res
        return  backtrack([],n,k,[])
        