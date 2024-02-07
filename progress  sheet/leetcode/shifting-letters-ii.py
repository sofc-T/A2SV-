class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        vals = [ord(chr) for chr in s]
        shift = [0] * len(s)

        for l,r,dir in shifts:
            if dir:
                shift[l] += 1
                if r + 1 < len(s):
                    shift[r+1] -= 1
            else:
                shift[l] -= 1
                if r + 1 < len(s):
                    shift[r+1] += 1
        running = 0
        for idx, val in enumerate(shift):
            running += val
            vals[idx] += running
            
        ords = []
        # print(shift)
        for val in vals:
            if val > 122:
                val = 97 + ((val - 123) % 26)
            elif val < 97:
                val = 122 - ((96 -val) % 26)
            ords.append(chr(val))
        return "".join(ords)