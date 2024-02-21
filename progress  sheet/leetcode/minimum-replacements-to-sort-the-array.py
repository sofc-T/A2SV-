class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        if len(nums) == 1 :return 0
        r, moves = len(nums) - 1, 0
        while r > 0:
            if nums[r] < nums[r-1]:
                
                spaces = ceil(nums[r-1] / nums[r])
                nums[r-1] = nums[r-1] // spaces
                moves += spaces - 1
                # print(spaces,nums,moves)
            else:
                r -= 1
        return moves
