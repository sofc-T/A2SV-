class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dest = {}
        orig = {}
        for numb, f, t in trips:
            if numb > capacity: return False
            if t in dest:
                dest[t] += numb
            else:
                dest[t] = numb
            if f in orig:
                orig[f] += numb
            else:
                orig[f] = numb
        points = sorted(list(set(list(dest.keys()) + list(orig.keys()))))
        curr = 0
        for val in points:
            if val in orig:
                curr += orig[val]
            if val in dest:
                curr -= dest[val]
            if curr > capacity:
                return False
        return True
        
        