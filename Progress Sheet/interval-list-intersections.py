class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        idx1, idx2 = 0, 0
        ans = []
        while idx1 < len(firstList) and idx2 < len(secondList):
            s1, e1,  = firstList[idx1]
            s2, e2 =  secondList[idx2]
            if e1 < s2 or e2 < s1:
                if s1 < s2:
                    idx1 += 1
                else:
                    idx2 += 1
            else:
                s = max(s1,s2)
                e = min(e1,e2) 
                ans.append([s,e])
                if e1 < e2: 
                    idx1 += 1
                else:
                    idx2 += 1
        return ans