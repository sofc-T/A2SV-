class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        i = 0
        quarter = len(arr) // 4 + 1
        while i < len(arr):
            c = 0
            temp = arr[i]
            while i < len(arr) and arr[i] == temp:
                c += 1
                i += 1
            if c >=quarter:
                return temp
