class Solution:
    def distanceBetweenBusStops(self, nums: List[int], start: int, destination: int) -> int:
        start, destination = min(start,destination), max(start,destination)
        return min(sum(nums[start:destination]),sum(nums[0:start])+sum(nums[destination:]))