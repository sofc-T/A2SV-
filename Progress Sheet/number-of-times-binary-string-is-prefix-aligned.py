class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxx = 0
        c = 0

        for i in range(len(flips)):
            maxx= max(flips[i],maxx)
            if maxx == i+1:
                c += 1
                
        return c