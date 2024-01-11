class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # l, r = k - 1,  len(cardPoints) - 1
        # max_sum = curr_sum = sum(cardPoints[:k])
        # while l > -1:
        #     curr_sum -= cardPoints[l]
        #     curr_sum += cardPoints[r]
        #     l -= 1
        #     r -= 1
        #     max_sum = max(max_sum, curr_sum)
        # return curr_sum

        nums = cardPoints[:k][::-1] + cardPoints[len(cardPoints)-k :][::-1]
        max_sum = curr_sum = sum(nums[:k])
        l, r= 0, k
        while r < len(nums):
            curr_sum -= nums[l]
            curr_sum += nums[r]
            l += 1
            r += 1
            max_sum = max(max_sum, curr_sum)
        return max_sum
