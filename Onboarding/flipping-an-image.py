class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        print(0 and 0)
        for row in image:
            l, r = 0, len(row) - 1
            while l <= r:
                if l == r:
                    row[l] = row[l] ^ 1
                else:
                    row[l], row[r] = row[r] ^ 1, row[l] ^ 1
                l += 1
                r -= 1
        return image