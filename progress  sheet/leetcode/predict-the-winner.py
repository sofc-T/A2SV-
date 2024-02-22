class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        a, b = 0 , 0
        l, r = 0, len(nums) - 1
        turn = "a"
        nums = tuple(nums)
        @cache
        def xo(l,r,a,b,turn):
            if l > r:
                return a >= b
            if turn == "a":
                return any((xo(l+1,r,a+nums[l],b,"b") , xo(l,r-1,a+nums[r],b,"b")))
            else:
                return all((xo(l+1,r,a,b+nums[l],"a"),xo(l,r-1,a,b+nums[r],"a")))
        return xo(l,r,a,b,"a")
            