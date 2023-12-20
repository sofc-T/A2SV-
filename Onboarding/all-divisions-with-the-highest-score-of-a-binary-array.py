class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        zeroes, ones = [0], [total]
        maxx = total
        zc, oc = 0, 0
        psum = 0
        maxxC = defaultdict(list)
        maxxC[total].append(0)
        for idx in range(len(nums)):
            psum += nums[idx]
            if nums[idx] == 0:
                zc += 1
            else:
                oc += 1
            zeroes.append(zc)
            ones.append(total - oc)
            maxx = max(zc+total-oc,maxx)
            maxxC[zc+total-oc].append(idx+1)
        return maxxC[maxx]