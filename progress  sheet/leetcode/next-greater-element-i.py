class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        store = {}
        for val in nums2:
            while stack and stack[-1] < val:
                store[stack.pop()] = val
            stack.append(val)
        for idx, num in enumerate(nums1):
            nums1[idx] = store.get(num,-1)
        return nums1