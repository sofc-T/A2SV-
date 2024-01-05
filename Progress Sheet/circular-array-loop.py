class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        print(nums)
        for i in range(len(nums)):
            seen = set()
            k, j = 0, i
            forward = 0
            while j not in seen:
                seen.add(j)
                if nums[j] > 0:
                    forward += 1
                    j = (j + nums[j]) % len(nums)
                else:
                    j += nums[j]
                    while j < 0:
                        j += len(nums)
                k += 1
            if k > 1 and j == i and (forward == 0 or forward == k):
                return True
        return False