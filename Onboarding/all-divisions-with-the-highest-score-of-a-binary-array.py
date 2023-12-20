class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        maxx = total
        zc, oc = 0, 0
        maxxC = defaultdict(list)
        maxxC[total].append(0)
        for idx in range(len(nums)):
            if nums[idx] == 0:
                zc += 1
            else:
                oc += 1
            maxx = max(zc+total-oc,maxx)
            maxxC[zc+total-oc].append(idx+1)
        return maxxC[maxx]