class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        bucket = [0] * 101
        for num in nums:
            bucket[num] += 1
        prev = 0
        for idx, val in enumerate(bucket):
            if bucket[idx] != 0:
                bucket[idx] = prev
                prev += val
                
        return [bucket[num]  for num in nums]