class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)   
        rabbits = 0
        for val in count:
            if val == 0:
                rabbits += count[val]
            elif count[val] <= val + 1:
                rabbits += val + 1
            else:
                rabbits +=  (ceil(count[val]/(val+1)) * (val + 1))
        return rabbits