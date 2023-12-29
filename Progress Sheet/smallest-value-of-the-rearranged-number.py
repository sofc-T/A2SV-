class Solution:
    def smallestNumber(self, num: int) -> int:
        if not num:return num
        nums = []
        zeroes = 0
        negative = False
        if num < 0:
            negative = True
            num *= -1
        while num:
            val = str(num%10)
            if val == "0":
                zeroes += 1
            else:
                nums.append(val)
            num //= 10
        nums.sort()
        if zeroes:
            if negative:
                return int("".join(nums[::-1]) + "0"*zeroes) * -1
            return int(nums[0] + "0" * zeroes + "".join(nums[1:]))
        return -1 * int("".join(nums[::-1])) if negative else int("".join(nums)) 