class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        res = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_val:
                res.append(True)
                # max_val = candies[i] + extraCandies
            else:
                res.append(False)
        return res