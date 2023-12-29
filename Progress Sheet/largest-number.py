class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        def comparator(s1,s2):
            if s1 + s2 > s2 + s1:
                return -1
            return 0
        from functools import cmp_to_key 
        nums = sorted(nums, key=cmp_to_key(comparator))
        return str(int("".join(nums)))