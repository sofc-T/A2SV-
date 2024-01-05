class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n, p, z = [], [], []
        
        for val in nums:
            if val > 0:
                p.append(val)
            elif val == 0:
                z.append(val)
            else:
                n.append(val)
        ps ,ns = set(p) , set(n)
        if len(z) >= 3:
            res.add((0,0,0))
        if z:
            for val in p:
                if -1 * val in set(n):
                    res.add((-1*val,0,val))
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in ps:
                    res.add(tuple(sorted([n[i],n[j],target])))
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in ns:
                    res.add(tuple(sorted([p[i],p[j],target])))
        return res