class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lisN = []
        lisP = []

        for i in nums:
            if i < 0:
                lisN.append(i)
            else:
                lisP.append(i)

        ans = []
        for i,j in zip(lisP, lisN):
            ans.append(i)
            ans.append(j)

        return ans
