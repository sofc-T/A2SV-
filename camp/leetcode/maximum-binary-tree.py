# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(nums):
            if not nums:
                return 

            idx = nums.index(max(nums))
            node = TreeNode(max(nums))
            node.right = build(nums[idx+1:])
            node.left = build(nums[0:idx])

            return node
        return build(nums)
