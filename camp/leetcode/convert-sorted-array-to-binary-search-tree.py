# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divide_conquer(l,r):
            if l > r:
                return
            mid = (r + l)  // 2
            root = TreeNode(nums[mid])

            root.left = divide_conquer(l,mid-1)
            root.right = divide_conquer(mid+1,r)
            return root
        return divide_conquer(0,len(nums)-1)