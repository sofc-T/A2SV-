class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        store = defaultdict(lambda :[0])
        occurences = Counter(nums)

        for idx,val in enumerate(nums):
            store[val].append(store[val][-1] + idx)

        for key in store:
            store[key] = list(reversed(store[key]))

            
        for idx,val in enumerate(nums):
            if occurences[val] == 1:
                nums[idx] = 0
            else:
                idx2 = len(store[val]) - 1
                left = abs((occurences[val] - len(store[val]) +1) * idx - store[val][-1])
                right = abs(store[val][0] - store[val][idx2] - ((len(store[val]) -1) * idx))
                nums[idx] =  left + right
                store[val].pop()

        return nums