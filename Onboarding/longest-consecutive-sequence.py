class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxL = 0
        while numset:
            l = 1
            num = numset.pop()
            temp = num
            while num + 1 in numset:
                l += 1
                num += 1
                numset.remove(num)
            num = temp
            while num - 1 in numset:
                num -= 1
                numset.remove(num)
                l += 1
            maxL = max(maxL,l)
        return maxL