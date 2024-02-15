class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        total, num = 0 , 0
        target, changes = 0, 0
        nums.append(inf)
        while total < n:
            if total >= nums[target]:
                total += nums[target]
                target += 1
            elif total >= num:
                num = total + 1
            elif nums[target] == num:
                total += num
                num += 1
                target += 1
            else:
                total += num
                changes += 1
            # print(total,changes,num)
        return changes