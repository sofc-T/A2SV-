class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        count = Counter(senate)
        r, d = count["R"], count["D"]
        stack = list(senate)
        dr, dd = 0 , 0
        stack = []
        while True:
            for senator in senate:
                if senator == "R":
                    if dr:
                        dr -= 1
                        if stack[-1] == "R":
                            stack.pop()
                    else:
                        d -= 1
                        dd += 1
                        stack.append("R")
                else:
                    if dd:
                        dd -= 1
                        if stack[-1] == "D":
                            stack.pop()
                    else:
                        r -= 1
                        dr += 1
                        stack.append("D")
                
                if d <= 0 or r <= 0:
                    break
            senate = stack
            if d <= 0:
                return "Radiant"
            if r <= 0:
                return "Dire"
        