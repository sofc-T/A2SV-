class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        lenn = len(set(nums))
        res,vals = 0, defaultdict(int)
        temp = 0
        for l in range(len(nums)):
            
            vals[nums[l]] += 1
            while len(vals) == lenn:
                res += len(nums) - l 
                # print(res,temp,l)
                vals[nums[temp]] -= 1
                if vals[nums[temp]] == 0:
                    del vals[nums[temp]]
                temp += 1
        return res