# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def traverse(root, low,high):
            if not root:
                return 0

            val = 0
            if root.val >= low and root.val <= high:
                val = root.val

            return val + traverse(root.left,low,high) + traverse(root.right,low,high)
        return traverse(root,low,high)
            