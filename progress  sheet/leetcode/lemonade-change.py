class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cinco, diez = 0 , 0 
        for bill in bills:
            if bill == 5:
                cinco += 1
            elif bill == 10:
                diez += 1
                cinco -= 1
            else:
                if diez > 0:
                    diez -= 1
                    cinco -= 1
                else:
                    cinco -= 3
            if cinco < 0 or diez < 0:
                return False
        return True